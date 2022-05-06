import re
import datetime
from collections import namedtuple
from bs4 import BeautifulSoup
import os
import sqlite3 as sq
from telegrame_save.db import request_index

file_html = f'../telegrame_save/data_html/{datetime.date.today().strftime("%Y-%m-%d")}.html'


def open_html():
        with open(file_html, 'r', encoding='koi8-u') as file:
            read_file = file.read()
            soup = BeautifulSoup(read_file, "lxml")
            body_telegrame = soup.find_all('pre')
            telegram = [re.sub(("\s+"), " ", i) for i in ['='.join(i) for i in body_telegrame]]
            telegram_gidro = []
            for i in request_index():
                index_g = int(i[0])
                # print(index_g)
            for x in telegram:
                index = int(x[20:26])
                # print(index)
                for x in telegram:
                    index = int(x[20:26])
                    if index_g - index == 0:
                        telegram_gidro.append([index,x[0:19], x[20:]])
                    if index_g == True:
                        telegram_gidro.append([index_g, None ])

            # print(telegram_gidro)
            # if not telegram:
            #     telegram_gidro.append([None])
            # yield telegram_gidro
            # for x in telegram:
            #      TelegramTuple = namedtuple('TelegramTuple','date_telegrame, telegram', defaults=None)
            #      telegram_gidro = TelegramTuple(x[0:19], x[20:])
            #      yield x[20:26], telegram_gidro



# def save_db():
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



if __name__ == '__main__':
    open_html()
    # save_db()
list_index = [int(i[0]) for i in request_index()]
print(list_index)
with open(file_html, 'r', encoding='koi8-u') as file:
    read_file = file.read()
    soup = BeautifulSoup(read_file, "lxml")
    body_telegrame = soup.find_all('pre')
    telegram = [re.sub(("\s+"), " ", i) for i in ['='.join(i) for i in body_telegrame]]
list_index_teleg =[int(x[20:26]) for x in  telegram]
# print(list_index_teleg)
print([x for x in telegram])
# h = zip(list_index, list_index_teleg)
# for x in h:
#     print(x)
# for x in open_html():
#     print(x)


# print({(datetime.datetime.today() + datetime.timedelta(days=-1).strftime("%Y-%m-%d %hh:%h:%ss"))})
#