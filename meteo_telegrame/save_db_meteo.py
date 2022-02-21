import re
from bs4 import BeautifulSoup
import os
import sqlite3 as sq
from meteo_telegrame.request_index_meteo import request_index_meteo

def open_html_meteo(index):
        with open(f'../meteo_telegrame/data_html/{index}.html', 'r', encoding='koi8-u') as file:
            r = file.read()
            soup = BeautifulSoup(r, "lxml")
            d = soup.find_all('pre')
            s = ['='.join(i) for i in d]
            telegram = [re.sub(("\s+"), " ", i) for i in s]
            telegram_meteo = []
            if telegram:
                for x in telegram:
                    telegram_meteo.append([x[0:19], x[20:]])

            if not telegram:
                telegram_meteo.append([None])
                # print(index,None)
            # print(telegram_meteo)
            yield telegram_meteo




def save_db_meteo():
    with sq.connect('../meteo_telegrame.db') as con:
        cur = con.cursor()
        for i in request_index_meteo():
            index = i[0]
            for s in open_html_meteo(index):
                if s[0][0] is not None:
                    for x in s:
                        date = x[0]
                        telegram = x[1]
                        cur.execute(f'''insert INTO '{index}'
                                    (date, meteo_telegrame)
                                    VALUES(?,?) ''', (date, telegram))
                if s[0][0] is None:
                    cur.execute(f'''insert INTO '{index}'
                                 (date, meteo_telegrame)
                                 VALUES(?,?) ''', (None, None))
                    print("No telegrame")
            con.commit()
            # os.remove(f'../telegrame_save/data_html/{index}.html')

save_db_meteo()






