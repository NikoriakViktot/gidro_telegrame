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
        not_telegram = list(set([int(x[20:26]) for x in telegram] +
                                [int(''.join(value[0])) for value in request_index()]))
        for x in telegram:
            telegram =x
            yield telegram




    def variable_telegrame_gidro(self):
        TelegramTuple = namedtuple('TelegramTuple', 'index, date_telegrame, telegram', defaults=None)
        for value in request_index():
            telegram_gidro = []
            for x in self.soup_file():
                variable_int = (int(value[0]) - int(x[20:26]))
                if variable_int == False:
                   telegram_gidro.append([TelegramTuple(x[20:26],x[0:19], x[20:])])
                else:
                    if variable_int == True:
                        continue
            yield telegram_gidro




    def variable_none(self):
        TelegramTuple = namedtuple('TelegramTuple', 'index, date_telegrame, telegram', defaults=None)
        telegram_server = list(set([(int(x[20:26])) for x in self.soup_file()]))
        telegram_server_not =[int(''.join(value[0])) for value in request_index()]

        not_telegram = list(set( telegram_server + telegram_server_not))
        print(len(not_telegram))

        print(len([''.join(value[0]) for value in request_index()]))
        print(len(set([x[20:26] for x in self.soup_file()])))
        nov = [x for x in self.variable_telegrame_gidro()]+ [TelegramTuple(z, None, None) for z in not_telegram]
        print(nov)


        # for x in self.variable_telegrame_gidro():
        #     tt = []
        #     if len(x):
        #         pass
        #     else:
        #         for z in not_telegram:
        #             # print(z)
        #             index_none = z
        #             tt.(TelegramTuple(index_none, None, None))
        #
        #     yield tt







            # yield telegram_gidro

  # for value in request_index():
            #     for x in telegram:
            #         if x is None:
            #             print(value)
            # telegram_gidro = TelegramTuple(x[20:26],x[0:19], x[20:])
if __name__ == '__main__':
    file_html = f'../telegrame_save/data_html/{datetime.date.today().strftime("%Y-%m-%d")}.html'
    f= '../telegrame_save/data_html/2022-05-24.html'
    s = Telegram_html(f)
    s.open_file()
    s.soup_file()
    s.variable_telegrame_gidro()
    s.variable_none()
    # for x in s.variable_none():
    #
    #     print(x)

