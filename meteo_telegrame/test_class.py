import re
import datetime
from collections import namedtuple
from bs4 import BeautifulSoup
import os
import sqlite3 as sq
from telegrame_save.db import request_index


class Telegram_html():

    def __init__(self,file):
       self.file = file



    def open_file(self):
        with open(self.file, 'r', encoding='koi8-u') as file:
            self.read_file = file.read()
            return self.read_file



    def soup_file(self):
        soup = BeautifulSoup(self.read_file, "lxml")
        body_telegrame = soup.find_all('pre')
        telegram = [re.sub(("\s+"), " ", i) for i in ['='.join(i) for i in body_telegrame]]
        TelegramTuple = namedtuple('TelegramTuple', 'index, date_telegrame, telegram', defaults=None)
        for x in telegram:
            telegram_gidro = TelegramTuple(x[20:26],x[0:19], x[20:])
            yield telegram_gidro



class Telegram_gidro():

    def __init__(self,index,date_telegrame,telegram):
        self.date_telegrame = date_telegrame
        self.index = index
        self.telegram = telegram



    def save_db_gidro(self):
        with sq.connect('../gauges_telegrame.db') as con:
            cur = con.cursor()
            date_last = (datetime.datetime.today() + datetime.timedelta(days=-1)).strftime("%Y-%m-%d")
            date_now = datetime.date.today().strftime("%Y-%m-%d")
            if self.date_telegrame[0:10] == date_now:
                date_n = self.date_telegrame
                telegram_n = self.telegram
                cur.execute(f'''insert INTO '{int(self.index)}'
                                (date, gauges_telegrame)
                               VALUES(?,?) ''', (date_n, telegram_n))
            if self.date_telegrame[0:10] == date_last:
                date_l = self.date_telegrame
                telegram_l = self.telegram
                cur.execute(f'''SELECT gauges_telegrame FROM '{int(self.index)}'
                          WHERE date = '{(datetime.datetime.today() + datetime.timedelta(days=-1)).strftime
                           ("%Y-%m-%d")} 08:00:00' ''')
                telegram_yesterday = cur.fetchone()
                if telegram_yesterday is None:
                    cur.execute(f''' insert INTO   '{int(self.index)}'
                               (date, gauges_telegrame)
                              VALUES(?,?) ''', (date_l, telegram_l))
                if telegram_yesterday is not None:
                    varif = telegram_l == telegram_yesterday[0]
                    if varif is True:
                        print(date_l, self.index)
                    else:
                        cur.execute(f''' update '{int(self.index)}' SET 
                                     gauges_telegrame = ?
                                     WHERE date = '{date_l}' ''', (telegram_l,))
                        print(date_now, self.index)
            con.commit()







if __name__ == '__main__':
    file_html = f'../telegrame_save/data_html/{datetime.date.today().strftime("%Y-%m-%d")}.html'
    s =  Telegram_html(file_html)
    s.open_file()
    for i in s.soup_file():
        for x in request_index():
            if int(x[0]) -  int(i.index) == False:
               object_t = Telegram_gidro(i.index, i.date_telegrame, i.telegram)
               object_t.save_db_gidro()

