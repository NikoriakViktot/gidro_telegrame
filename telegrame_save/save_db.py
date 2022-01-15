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
            print(telegram)
            return telegram


def pars_telegram():
    telegram_html = open_html()
    date_telegram = [i[26:32] for i in telegram_html]
    print(date_telegram)





def request_index():
    with sq.connect('../gauges_telegrame.db') as con:
        cur = con.cursor()
        cur.execute("SELECT * FROM index_gauges")
        index = [x[0] for x in cur.fetchall()]
        for value in index:
            INDEX = []
            INDEX.append(value)
            yield INDEX



for i in request_index():
    open_html(i[0])

pars_telegram()