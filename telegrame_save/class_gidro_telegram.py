import datetime
from telegrame_save.class_db import Database
from telegrame_save.class_html import Telegram_html


class Telegram_gidro(Database):

    insert_gidro_telegram = 'insert INTO gidro_telegram' \
                            '(index_hydro_station ,date,gauges_telegrame)' \
                            ' VALUES(?,?,?)'



    def __init__(self, index: object, date_telegrame: object, telegram: object, **kwargs: object) -> object:
        super().__init__(**kwargs)
        self.date_telegrame = date_telegrame
        self.index = index
        self.telegram = telegram



    def save_db_gidro(self):
        date_last = (datetime.datetime.today() + datetime.timedelta(days=-1)).strftime("%Y-%m-%d")
        date_now = datetime.date.today().strftime("%Y-%m-%d")
        telegram_now = self.select_date(self.index,date=0)
        if telegram_now is None:
            if self.date_telegrame[0:10] == date_now:
                index = int(self.index)
                date_n = self.date_telegrame
                telegram_n = self.telegram
                self.database_query(self.insert_gidro_telegram,index,date_n,telegram_n)
        if self.date_telegrame[0:10] == date_last:
            index = int(self.index)
            date_l = self.date_telegrame
            telegram_l = self.telegram
            self.select_date(index, -1)
            telegram_yesterday =  self.select_date(index, -1)
            if telegram_yesterday is None:
                self.database_query(self.insert_gidro_telegram, index, date_l, telegram_l)
                if telegram_yesterday is not None:
                    varif = telegram_l == telegram_yesterday
                    if varif is True:
                        print(date_l, self.index)
                    else:
                        self.update(index,telegram_l,-1)


if __name__ == '__main__':
    file_html = f'../telegrame_save/data_html/{datetime.date.today().strftime("%Y-%m-%d")}.html'
    # date_remove = (datetime.datetime.today() + datetime.timedelta(days=-1)).strftime("%Y-%m-%d")
    s = Telegram_html(file_html)
    s.open_file()
    for i in s.soup_file():
       dict_gidro_base = { 'filename':'../gauges_telegrame1.db',
                            'table':'gidro_telegram' }
       Telegram_gidro(i.index, i.date_telegrame, i.telegram, **dict_gidro_base).save_db_gidro()

