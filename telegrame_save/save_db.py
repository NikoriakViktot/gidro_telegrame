import re
from bs4 import BeautifulSoup
import sqlite3 as sq
from telegrame_save.request_index import request_index

def open_html(index):
        with open(f'../telegrame_save/data_html/{index}.html', 'r', encoding='koi8-u') as file:
            r = file.read()
            soup = BeautifulSoup(r, "lxml")
            d = soup.find_all('pre')
            s = ['='.join(i) for i in d]
            telegram = [re.sub(("\s+"), " ", i) for i in s]
            for x in telegram:
                try:
                    yield x[0:19], x[20:]

                except TypeError:
                    yield None



def save_db():
    with sq.connect('../gauges_telegrame.db') as con:
        cur = con.cursor()
        for i in request_index():
            index = i[0]
            for s in open_html(index):
                date = s[0]
                telegram = s[1]
                cur.execute(f'''insert INTO '{index}'
                            (date, gauges_telegrame)
                            VALUES(?,?) ''', (date, telegram))
                con.commit()

save_db()






