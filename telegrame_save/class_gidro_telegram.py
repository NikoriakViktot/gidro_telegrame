import re
import datetime
from collections import namedtuple
from bs4 import BeautifulSoup
import os
import sqlite3 as sq
from telegrame_save.class_db import Database
from telegrame_save.db import request_index

class Telegram_gidro():

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
                        break
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

class Telegram_gidro():

    def __init__(self, index, date_telegrame, telegram):
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
    f= '../telegrame_save/data_html/2022-07-01.html'
    file_db_gidro = '../gauges_telegrame1.db'
    insert_gidro_telegram = 'insert INTO gidro_telegram' \
                            '(index_hydro_station ,date,gauges_telegrame)' \
                            ' VALUES(?,?,?)'
    s = Telegram_html(file_html)
    s.open_file()
    # for i in s.soup_file():
    #     for x in request_index():
    #         if int(x[0]) -  int(i.index) == False:
    #            object_t = Telegram_gidro(i.index, i.date_telegrame, i.telegram)
    #            object_t.save_db_gidro()
    gidro_telgram_tabl = Database(filename=file_db_gidro, table='gidro_telegram')
    for i in s.soup_file():
        # print(i)
        a,b,c = i.index, i.date_telegrame, i.telegram
        object_t = Telegram_gidro(i.index, i.date_telegrame, i.telegram)
        # print(object_t)

        gidro_telgram_tabl.database_query(insert_gidro_telegram, int(a),b,c)
        # for row in gidro_telgram_tabl:
        #     print(dict(row))
    t =gidro_telgram_tabl.select_date(index=42130, date=-1)
    print(t[0])


    ddd = 'SELECT gauges_telegrame FROM gidro_telegram WHERE index_hydro_station= 42130 and  date= 2022-05-23 08:00:00'




    # for x in s.variable_none():

    #
    #     print(x)

