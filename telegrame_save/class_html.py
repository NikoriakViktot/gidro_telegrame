import re
from collections import namedtuple
from bs4 import BeautifulSoup
from selenium_gidro.class_driver import SeleniumGidro
import os


class Telegram_html(SeleniumGidro):

    def __init__(self):
       # self.date_remove = date_remove
       super().__init__()





    def open_file(self):
        with open(self.data_html, 'r', encoding='koi8-u') as file:
            self.read_file = file.read()

            return self.read_file
    # def remove_file(self):
    #     os.remove(f'../telegrame_save/data_html/{self.date_remove}.html')



    def soup_file(self):
        soup = BeautifulSoup(self.read_file, "lxml")
        body_telegrame = soup.find_all('pre')
        telegram = [re.sub(("\s+"), " ", i) for i in ['='.join(i) for i in body_telegrame]]
        TelegramTuple = namedtuple('TelegramTuple', 'index, date_telegrame, telegram', defaults=None)
        for x in telegram:
            telegram = TelegramTuple(x[20:26], x[0:19], x[20:])
            yield telegram


