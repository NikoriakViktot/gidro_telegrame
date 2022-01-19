import datetime
import re
from bs4 import BeautifulSoup
import sqlite3 as sq
from telegrame_save.request_index import request_index
import json
import itertools

from collections import ChainMap

def select_telegrame():
    for i in request_index():
        index_i = int(i[0])
        # print(index_i)
        with sq.connect('../gauges_telegrame.db') as con:
            cur = con.cursor()
            cur.execute(f"SELECT date, gauges_telegrame FROM '{index_i}'" )
            # data = cur.fetchall()
            body_telegram = (x for x in cur.fetchall())
            # print(data[0][1])
            # print( body_telegram)
            for x in  body_telegram:
                print(str(x[0]).split(' '))
                # print(x[1])
                print(str(x[1]).split(' '))
                # if x == None:
                    # print(x)


select_telegrame()

    # def open_html(self):
    #     with open(f'E:\ВІТЯ\gidro_bot\data_html\{datetime.date.today().strftime("%Y-%m-%d")}.html', 'r', encoding='koi8-u') as file:
    #         r = file.read()
    #         soup = BeautifulSoup(r, "lxml")
    #         d = soup.find_all('pre')
    #         s = ['='.join(i) for i in d]
    #         telegrams = [re.sub(("\s+"), " ", i) for i in s]
    #         return telegrams
    #
    #
    #
    # def pars_telegram(self):
    #     self.list_telegrams =  self.open_html()
    #     self.index_post = [i[20:26] for i in self.list_telegrams]
    #     self.date_telegrame =  [i[26:32] for i in self.list_telegrams]
    #     self.date_time_report = [i[0:20] for i in self.list_telegrams]
    #     self.date_time_report_dict =  dict(zip(self.index_post, [i[0:20] for i in self.list_telegrams]))
    #     self.temperatur = dict(zip(self.index_post, [i[30:35] for i in self.list_telegrams]))
    #     self.change_level  = [i[18:23] for i in self.list_telegrams]
    #     return self
    #
    #
    #
    # def telegram_split(self)->list:
    #     for x in self.pars_telegram().date_telegrame:
    #         d = ''.join(x)
    #         patern_date = re.compile(f'{datetime.date.today().strftime("%d")}081|'
    #                                  f'{datetime.date.today().strftime("%d")}082|'
    #                                  f'{datetime.date.today().strftime("%d")}083|'
    #                                  f'{datetime.date.today().strftime("%d")}087')
    #         if d[0:2] == datetime.date.today().strftime("%d"):
    #             telegrams_with_date = re.sub(patern_date,'',' '.join(self.list_telegrams))
    #             telegrams_oprac = telegrams_with_date.split("=")
    #
    #     return telegrams_oprac
    #
    #
    #
    # def parsing_telegram_water_level_08_00(self):
    #     level_morning_iterable = [re.findall('(1\d{4})', i) for i in self.telegram_split()]
    #     l_m_join = [' '.join(i) for i in level_morning_iterable]
    #     level_morning = []
    #     for i in l_m_join:
    #         if i.isnumeric():
    #             t = ''.join(i)
    #             if i in t:
    #                 c = ((int(i) - 10000) - 5000)
    #                 if c <= 0:
    #                     level_morning.append(c + 5000)
    #                 if c >= 0:
    #                     level_morning.append(-c)
    #     return level_morning
    #
    #
    #
    # def parsing_telegram_water_level_20_00(self):
    #     level_evening_iterable = [i for i in [re.findall('(3\d{4})', i) for i in self.telegram_split()]]
    #     l_v_join = [' '.join(i)  for i in level_evening_iterable]
    #     level_evening = []
    #     for i in l_v_join:
    #         if i.isnumeric():
    #             t = ''.join(i)
    #             if i in t:
    #                 c = ((int(i) - 30000)-5000)
    #                 if c <=0:
    #                     level_evening.append(c+5000)
    #                 if c >=0:
    #                     level_evening.append(-c)
    #     return level_evening
    #
    #
    #
    # def preciptation(self):
    #     precipitation = dict(zip(self.pars_telegram().index_post, [i for i in [re.findall('(0\d{4}|0\d{3}/)', i) for i in self.telegram_split()]]))
    #     return precipitation
    #
    #
    #
    # def precipitation_0_24(self):
    #     pricip_doba = [v[:1] for v in self.preciptation().values()]
    #     rozpakovanuy_pricip_doba = []
    #     for v in pricip_doba:
    #         ind = "".join(v)
    #         rozpakovanuy_pricip_doba.append(ind)
    #     opadu_doba = [f[1:4] for f in rozpakovanuy_pricip_doba]
    #     opadu_doba_int = []
    #     for i in opadu_doba:
    #         if i.isnumeric():
    #             t = ''.join(i)
    #             if i in t:
    #                 c = int(i) - 900
    #                 if c >= 0:
    #                     opadu_doba_int.append(float((c - 90)/10))
    #                     continue
    #                 if c <= 0:
    #                     opadu_doba_int.append(int(c)+900)
    #                     continue
    #         if i is not i.isnumeric():
    #             p = None
    #             opadu_doba_int.append(p)
    #     return opadu_doba_int
    #
    #
    #
    #
    # def precipitation_08_20(self):
    #     pricip_den = [v[1:2] for v in self.preciptation().values()]
    #     rozpakovanuy_pricip_den = []
    #     for v in pricip_den:
    #         ind = " ".join(v)
    #         rozpakovanuy_pricip_den.append(ind)
    #     opadu_den = [f[1:4] for f in rozpakovanuy_pricip_den]
    #     opadu_den_int = []
    #     for i in opadu_den:
    #         if i.isnumeric():
    #             t = ''.join(i)
    #             if i in t:
    #                 c = int(i) - 900
    #                 if c >=0:
    #                     opadu_den_int.append(float((c - 90)/10))
    #                     continue
    #                 if c <=0:
    #                     opadu_den_int.append(int(c)+900)
    #                     continue
    #         if i is not i.isnumeric():
    #             p = None
    #             opadu_den_int.append(p)
    #     return opadu_den_int
    #
    #
    #
    # def tuple_report(self):
    #     tuple_report = [i for i in zip(self.pars_telegram().index_post,
    #                  self.pars_telegram().date_time_report,
    #                  self.parsing_telegram_water_level_08_00(),
    #                  self.parsing_telegram_water_level_20_00(),
    #                  self.precipitation_0_24(),
    #                  self.precipitation_08_20())]
    #     return tuple_report
    #
    #
    #
    #
    # def munual_save(self, p)->PostRoportManual:
    #     ind = p[0]
    #     post = GidroPost.objects.get(index_posta=ind)
    #     date = p[1]
    #     yy, mm, dd = date[0:10].split('-')
    #     hh, m, ss = date[11:19].split(':')
    #     repdata = datetime.datetime(int(yy),
    #                                 month=int(mm),
    #                                 day=int(dd),
    #                                 hour=int(hh),
    #                                 minute=int(m),
    #                                 second=int(ss))
    #
    #     l_8= p[2]
    #     l_20 = p[3]
    #     p_dob = p[4]
    #     p_den = p[5]
    #     return (post = post,report_time = repdata, water_level_08_00 = l_8,
    #                                  water_level_20_00 = l_20, precipitation_doba= p_dob,
    #                                  precipitation_den= p_den)
    #
    #
    #
    #
    # def handle(self, *args, **options):
    #     for i in self.tuple_report():
    #         try:
    #             report = self.munual_save(i)
    #             report.save()
    #             print(f'save {report}')
    #
    #         except:
    #             print(f'not save')
    #
    #

