import datetime
from selenium_gidro.class_driver import SeleniumGidro
from telegrame_save.class_db import Database
from telegrame_save.class_html import Telegram_html


class Telegram_gidro(Database):
    insert_gidro_telegram = 'insert INTO gidro_telegram' \
                            '(index_hydro_station ,date,gauges_telegrame)' \
                            ' VALUES(?,?,?)'




    def __init__(self, index_post, date_telegrame, telegram, **kwargs):
        super().__init__(**kwargs)
        self.date_telegrame = date_telegrame
        self.index_post = index_post
        self.telegram = telegram



    def save_db_gidro(self):
        date_last = (datetime.datetime.today() + datetime.timedelta(days=-1)).strftime("%Y-%m-%d")
        date_now = datetime.date.today().strftime("%Y-%m-%d")
        telegram_now = self.select_date(self.index_post,date=0)
        if telegram_now is None:
            if self.date_telegrame[0:10] == date_now:
                index = int(self.index_post)
                date_n = self.date_telegrame
                telegram_n = self.telegram
                self.database_query(self.insert_gidro_telegram,index,date_n,telegram_n)
        if self.date_telegrame[0:10] == date_last:
            index = int(self.index_post)
            date_l = self.date_telegrame
            telegram_l = self.telegram
            self.select_date(index, -1)
            telegram_yesterday =  self.select_date(index, -1)
            if telegram_yesterday is None:
                self.database_query(self.insert_gidro_telegram, index, date_l, telegram_l)
                if telegram_yesterday is not None:
                    varif = telegram_l == telegram_yesterday
                    if varif is True:
                        print(date_l, self.index_post)
                    else:
                        self.update(index,telegram_l,-1)


if __name__ == '__main__':
    def index_gidropost() -> str:
        i = []
        file = '../gauges_telegrame1.db'
        for value in Database(filename=file, table='index_gauges'):
            i.append(value[0])
        index = ' '.join(i)
        return index
    SeleniumGidro().post_gidro_telegrame_all(index_gidropost())
    s = Telegram_html().open_file()
    for i in s.soup_file():
       dict_gidro_base = { 'filename':'../gauges_telegrame1.db',
                            'table':'gidro_telegram' }
       Telegram_gidro(i.index, i.date_telegrame, i.telegram, **dict_gidro_base).save_db_gidro()

