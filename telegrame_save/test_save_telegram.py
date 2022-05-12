import re
import datetime
from collections import namedtuple
from bs4 import BeautifulSoup
import os
import sqlite3 as sq
from telegrame_save.db import request_index


class Telegram_html():

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


    def verification_telegram_date_now(self):
        for x in self.soup_file():
            date_now = datetime.date.today().strftime("%Y-%m-%d")
            date_last = (datetime.datetime.today() + datetime.timedelta(days=-1)).strftime("%Y-%m-%d")
            TelegramNow = namedtuple('TelegramNow', 'index, date_telegrame, telegram', defaults=None)
            TelegramLast = namedtuple('TelegramLast', 'index, date_telegrame, telegram', defaults=None)
            if x.date_telegrame[0:10]  == date_now:
                self.telegrame_now = TelegramNow(x.index,x.date_telegrame,x.telegram)
                yield self.telegrame_now
            # if x.date_telegrame[0:10]  == date_last:
            #     self.telegrame_last = TelegramLast(x.index,x.date_telegrame,x.telegram)
            #     yield self.telegrame_last
                # return self.telegrame_now, self.telegrame_last

    def verification_telegram_index(self):
        for value in request_index():
            TelegramNowIndex = namedtuple('TelegramNowIndex', 'index, date_telegrame, telegram', defaults=None)
            TelegramLastIndex = namedtuple('TelegramLastIndex', 'index, date_telegrame, telegram', defaults=None)
            # print(value[0])
            self.telegrame_now_ind = []

            if self.verification_telegram_date_now():
                for x in self.verification_telegram_date_now():
                    self.telegrame_now_ind.append(TelegramNowIndex(x.index, x.date_telegrame, x.telegram))

                # print(x.index)

                    # if int(x.index) - int(value[0]) == 0:

                #
                if not self.verification_telegram_date_now():
                   self.telegrame_now_ind.append(TelegramNowIndex(value[0],x.date_telegrame, None))
                    # print(self.telegrame_now_ind)
                yield self.telegrame_now_ind





    # def save_db(self):
            #     with sq.connect('../gauges_telegrame.db') as con:
            #         cur = con.cursor()
            #
            #             for s in open_html():
            #                 # index = int(s[0])
            #                 # print(index)
            #                 print(s)
            # date = s[1].date_telegrame[0:10]
            # telegram = s[1].telegram
            # cur.execute(f'''SELECT gauges_telegrame FROM '{index}'
            #           WHERE date in (date('{(datetime.datetime.today() + datetime.timedelta(days=-1)).strftime
            #            ("%Y-%m-%d")}'))  ''')
            # telegram_yesterday = cur.fetchone()
            # print(telegram_yesterday[0])

            # cur.execute(f'''insert INTO '{index}'
            #                 (date, gauges_telegrame)
            #                 VALUES(?,?) ''', (date, telegram))
            # con.commit()
            # os.remove(f'../telegrame_save/data_html/{index}.html')







            # print(x.date_telegrame[0:10])





if __name__ == '__main__':
    file_html = f'../telegrame_save/data_html/{datetime.date.today().strftime("%Y-%m-%d")}.html'
    s = Telegram_html(file_html)
    s.open_file()

    # v = s.verification_telegram_date()
    v = s.verification_telegram_index()
    # aa =
    for x in v:
        print(x)
    #
    # for x in s.telegrame_last:
    #     print(x)
    # for x in s.soup_file():
    #     print()
