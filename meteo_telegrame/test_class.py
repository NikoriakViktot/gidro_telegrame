import re
import datetime
from collections import namedtuple
from bs4 import BeautifulSoup
import os
import sqlite3 as sq
from telegrame_save.db import request_index
from telegrame_save.class_html import Telegram_html

class Telegram_gidro():

    def __init__(self,index,date_telegrame,telegram):
        self.date_telegrame = date_telegrame
        self.index = index
        self.telegram = telegram




    def verification_telegram_date_now(self):

       date_now = datetime.date.today().strftime("%Y-%m-%d")
       date_last = (datetime.datetime.today() + datetime.timedelta(days=-1)).strftime("%Y-%m-%d")
       TelegramNow = namedtuple('TelegramNow', 'index, date_telegrame, telegram', defaults=None)
       TelegramLast = namedtuple('TelegramLast', 'index, date_telegrame, telegram', defaults=None)
       if self.date_telegrame[0:10]  == date_now:
           self.telegrame_now = TelegramNow(self.index,self.date_telegrame,self.telegram)
           # print(self.telegrame_now)
           return self.telegrame_now
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

    def save_db_gidro(self, index):

        with sq.connect('../gauges_telegrame.db') as con:
            cur = con.cursor()
            index_gaqauses = index
            # print(index_gaqauses)
            date_now = datetime.date.today().strftime("%Y-%m-%d")
            if int(index_gaqauses) - int(self.index) == 0:
                if self.date_telegrame[0:10] == date_now:
                    date = self.date_telegrame
                    telegram = self.telegram
                    # print(index_gaqauses)
                #
                    print('telegrame ',date,index, telegram)
                #     cur.execute(f'''insert INTO '{self.index}'
                #                       (date, gauges_telegrame)
                #                     VALUES(?,?) ''', (date, telegram))

                # if index_gaqauses not in self.index:
                #     print(index_gaqauses)
                #     print("No telegrame")
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
    s =  Telegram_html(file_html)
    s.open_file()
    for i in s.soup_file():
        for x in request_index():
            object_t = Telegram_gidro(i.index,i.date_telegrame,i.telegram)
            object_t.save_db_gidro(x[0])

            # print(x)


            # for d in s.verification_telegram_date_now():
            # print(d)
