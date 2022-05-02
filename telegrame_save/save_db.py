import re
import datetime
from collections import namedtuple
from bs4 import BeautifulSoup
import os
import sqlite3 as sq
from telegrame_save.request_index import request_index

def open_html():
        with open(f'../telegrame_save/data_html/{datetime.date.today().strftime("%Y-%m-%d")}.html', 'r', encoding='koi8-u') as file:
            read_file = file.read()
            soup = BeautifulSoup(read_file, "lxml")
            body_telegrame = soup.find_all('pre')
            telegram = [re.sub(("\s+"), " ", i) for i in ['='.join(i) for i in body_telegrame]]
            for x in telegram:
                 TelegramTuple = namedtuple('TelegramTuple','date_telegrame, telegram', defaults=None)
                 telegram_gidro = TelegramTuple(x[0:19], x[20:])
                 yield x[20:26], telegram_gidro



def save_db():
    with sq.connect('../gauges_telegrame.db') as con:
        cur = con.cursor()
        cur.execute(f'''SELECT gauges_telegrame FROM '{index}' 
                                  WHERE date in (date('{(datetime.datetime.today() + datetime.timedelta(days=-1)).strftime
        ("%Y-%m-%d")}'))  ''')
        telegram_yesterday = cur.fetchone()
        print(telegram_yesterday[0])


        for s in open_html():
            index = int(s[0])
            # print(index)
            date = s[1].date_telegrame[0:10]
            telegram = s[1].telegram
            cur.execute(f'''SELECT gauges_telegrame FROM '{index}' 
                          WHERE date in (date('{(datetime.datetime.today() + datetime.timedelta(days=-1)).strftime
                           ("%Y-%m-%d")}'))  ''')
            telegram_yesterday = cur.fetchone()
            print(telegram_yesterday[0])

            # cur.execute(f'''insert INTO '{index}'
            #                 (date, gauges_telegrame)
            #                 VALUES(?,?) ''', (date, telegram))
            # con.commit()
            # os.remove(f'../telegrame_save/data_html/{index}.html')

save_db()


# for x in open_html():
#     print(x)


# print({(datetime.datetime.today() + datetime.timedelta(days=-1).strftime("%Y-%m-%d %hh:%h:%ss"))})
#