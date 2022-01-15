import re
from bs4 import BeautifulSoup

def open_html():
        with open(f'\data_html\data.html', 'r', encoding='koi8-u') as file:
            r = file.read()
            soup = BeautifulSoup(r, "lxml")
            d = soup.find_all('pre')
            s = ['='.join(i) for i in d]
            telegrams = [re.sub(("\s+"), " ", i) for i in s]
            return telegrams

