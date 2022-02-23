import sqlite3 as sq
from meteo_telegrame.request_index_meteo import request_index_meteo
import re
from openpyxl import load_workbook
from openpyxl import Workbook


def select_telegrame_meteo():
    for i in request_index_meteo():
        index_i = i[0]
        with sq.connect('../meteo_telegrame.db') as con:
            cur = con.cursor()
            cur.execute(f"SELECT date, meteo_telegrame FROM '{index_i}'" )
            body_telegram = [x for x in cur.fetchall()]
            yield index_i,body_telegram



def telegram_report_meteo():
    report_telegrame_meteo = []
    for x in  select_telegrame_meteo():
        index_station =x[0]
        date = x[1][0][0]
        if date  is None:
            report_telegrame_meteo.append((index_station, 'Телеграми відсутні'))
        if date is not None:
            report_telegrame_meteo.append((index_station, "Телеграми надсилаються"))
    return report_telegrame_meteo


#
#
def report_station_xls():
    wb = Workbook()
    ws = wb.active
    for x in telegram_report_meteo():
        ws.append(x)
    wb.save('report_station.xlsx')










print(telegram_report_meteo())
report_station_xls()