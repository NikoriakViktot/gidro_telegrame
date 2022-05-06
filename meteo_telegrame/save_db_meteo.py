import re
from bs4 import BeautifulSoup

import sqlite3 as sq
from meteo_telegrame.request_index_meteo import request_index_meteo

data_html = f'../meteo_telegrame/data_html/{index}.html

def open_html_meteo(index):
        with open(data_html, 'r', encoding='koi8-u') as file:
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
                        print(telegram)
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


if __name__ == '__main__':
    save_db_meteo()






