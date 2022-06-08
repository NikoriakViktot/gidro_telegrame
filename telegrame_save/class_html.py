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
        for value in request_index():
            telegram_gidro= []
            for x in telegram:
                variable_int = (int(value[0]) - int(x[20:26]))
                variable_str = (value[0] is not x[20:26])
                # print(variable_int)
                # print(variable_str)
                # if variable_int == False:
                    # telegram_gidro.append([TelegramTuple(x[20:26],x[0s:19], x[20:])])
                    # if variable_int == True:
                    #     continue

            for x in telegram:
                for value in request_index():
                    if value[0] is not x[20:26]:
                        print(value)
            # telegram_gidro = TelegramTuple(x[20:26],x[0:19], x[20:])
            # yield telegram_gidro


if __name__ == '__main__':
    file_html = f'../telegrame_save/data_html/{datetime.date.today().strftime("%Y-%m-%d")}.html'
    f= '../telegrame_save/data_html/2022-05-24.html'
    s = Telegram_html(f)
    s.open_file()
    print(s.soup_file())