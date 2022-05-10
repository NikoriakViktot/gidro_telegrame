import re
import datetime
from collections import namedtuple
from bs4 import BeautifulSoup
import os
import sqlite3 as sq
from telegrame_save.db import request_index


class Telegram_html:

    def __init__(self, file):
        self.file = file



    def open_file(self):
        with open(self.file, 'r', encoding='koi8-u') as file:
            self.read_file = file.read()
            return self.read_file



    def soup_file(self):
        soup = BeautifulSoup(self.read_file, "lxml")
        body_telegrame = soup.find_all('pre')
        self.telegram = [re.sub(("\s+"), " ", i) for i in ['='.join(i) for i in body_telegrame]]
        TelegramTuple = namedtuple('TelegramTuple', 'index, date_telegrame, telegram', defaults=None)
        for x in self.telegram:
            self.tegram_gidro = TelegramTuple(x[20:26],x[0:19], x[20:])
            yield self.tegram_gidro


    def verification_telegram(self):
        for x in self.soup_file():
            date_now = datetime.date.today().strftime("%Y-%m-%d")
            date_last = (datetime.datetime.today() + datetime.timedelta(days=-1)).strftime("%Y-%m-%d")
            if x.date_telegrame[0:10]  == date_now:
                self.telegrame_now = x.index,x.date_telegrame,x.telegram
                yield self.telegrame_now
            if x.date_telegrame[0:10]  == date_last:
                self.telegrame_last = x.index,x.date_telegrame,x.telegram
                yield self.telegrame_last






            # print(x.date_telegrame[0:10])





if __name__ == '__main__':
    file_html = f'../telegrame_save/data_html/{datetime.date.today().strftime("%Y-%m-%d")}.html'
    s = Telegram_html(file_html)
    s.open_file()
    v = s.telegrame_now
    # v = s.verification_telegram()
    for x in v:
        print(x)
    #
    # for x in s.telegrame_last:
    #     print(x)
    # for x in s.soup_file():
    #     print()
