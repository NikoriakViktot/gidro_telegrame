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


# if __name__ == '__main__':
#     # file_html = f'../telegrame_save/data_html/{datetime.date.today().strftime("%Y-%m-%d")}.html'
#     # s = Telegram_html(file_html)
#     # s.open_file()
#     # s.soup_file()