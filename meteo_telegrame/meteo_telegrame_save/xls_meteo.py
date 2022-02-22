import sqlite3 as sq
from meteo_telegrame.request_index_meteo import request_index_meteo
import re
from openpyxl import Workbook


def select_telegrame_meteo():
    for i in request_index_meteo():
        print(i)

        index_i = i[0]
        print(index_i)

        # with sq.connect('../meteo_telegrame.db') as con:
        #     cur = con.cursor()
        #     cur.execute(f"SELECT date, meteo_telegrame FROM '{index_i}'" )
        #     body_telegram = [x for x in cur.fetchall()]
        #     yield body_telegram



# def telegram_report_meteo():
#     for x in  select_telegrame_meteo():
#         print(x)
#
#         if not len(x) == 0:
#             if isinstance(x[0], tuple) == True:
#                 date = x[0][0]
#                 telegram_valid = [re.sub(("="), "", i) for  i in
#                                   [y for y in str(x[0][1]).split(' ')]]
#                 return  date, telegram_valid

#
#
# for x in telegram_report_meteo():
#     print(x[1])
# for x in select_telegrame_meteo():
#     print(x)
select_telegrame_meteo()
# print(telegram_report_meteo())