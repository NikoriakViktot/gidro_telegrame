import re
import datetime
from collections import namedtuple
from bs4 import BeautifulSoup
import os
import sqlite3 as sq
from telegrame_save.db import request_index


class Telegram_html():

    def __init__(self,index):
        self.index = index
        # self.file = file



    def open_file(self, file):
        with open(file, 'r', encoding='koi8-u') as file:
            self.read_file = file.read()
            return self.read_file



    def soup_file(self,index_gaqauses):
        soup = BeautifulSoup(self.read_file, "lxml")
        body_telegrame = soup.find_all('pre')
        telegram = [re.sub(("\s+"), " ", i) for i in ['='.join(i) for i in body_telegrame]]
        TelegramTuple = namedtuple('TelegramTuple', 'index, date_telegrame, telegram', defaults=None)
        if telegram:
            for x in telegram:
                if int(index_gaqauses) - int(x[20:26]) == 0:
                    telegram_gidro = TelegramTuple(index_gaqauses,x[0:19], x[20:])

                    print(telegram_gidro)

                #
                #
                # yield telegram_gidro


    def verification_telegram_date_now(self):
        for x in self.soup_file():
            # print(x)
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



    # def verification_telegram_index(self):
    #     self.telegrame_now_ind = []
    #     for x in self.verification_telegram_date_now():
    #         TelegramNowIndex = namedtuple('TelegramNowIndex', 'index, date_telegrame, telegram', defaults=None)
    #
    #
    #
    #
    #         if x.index == self.index:
    #              self.telegrame_now_ind.append(TelegramNowIndex(x.index, x.date_telegrame, x.telegram))
    #
    #         if self.index !=  x.index:
    #                     # print(value)
    #             # if value[0] is not x.index:
    #              self.telegrame_now_ind.append(TelegramNowIndex(self.index,x.date_telegrame, None))
    #              # yield self.telegrame_now_ind
    #
    #         # TelegramLastIndex = namedtuple('TelegramLastIndex', 'index, date_telegrame, telegram', defaults=None)
    #         # # print(value[0])
    #

    def save_db_gidro(self):

        with sq.connect('../gauges_telegrame.db') as con:
            cur = con.cursor()
            # if index_gaqauses == self.index:
            #     print(index_gaqauses)
            for i in self.verification_telegram_date_now():
                # if index_gaqauses == i.index:
                    # if i.index is not None:
                    date = i.date_telegrame
                    telegram = i.telegram
                    # print(index_gaqauses)
                #
                    print('telegrame ',self.index, telegram)
                #     cur.execute(f'''insert INTO '{self.index}'
                #                       (date, gauges_telegrame)
                #                     VALUES(?,?) ''', (date, telegram))

                # if self.index:
                    # print(index_gaqauses)
                    print("No telegrame")
                    # cur.execute(f'''insert INTO '{self.index}'
                    #                  (date, gauges_telegrame)
                    #                  VALUES(?,?) ''', (None, None))


    # def save_db(self):
    #             with sq.connect('../gauges_telegrame.db') as con:
    #                 cur = con.cursor()
    #
    #                     for s in open_html():
    #                         # index = int(s[0])
    #                         # print(index)
    #                         print(s)
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
    # s = Telegram_html(file_html)
    # s.open_file()

    # v = s.verification_telegram_date()
    # v = s.verification_telegram_index()
    # aa =
    for x in request_index():
        s = Telegram_html(x[0])
        s.open_file(file_html)
        s.soup_file(x[0])
        s.save_db_gidro()

        print(x[0])


            # for d in s.verification_telegram_date_now():
            # print(d)
