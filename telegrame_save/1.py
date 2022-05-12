def verification_telegram_date(self):
    for x in self.soup_file():
        date_now = datetime.date.today().strftime("%Y-%m-%d")
        date_last = (datetime.datetime.today() + datetime.timedelta(days=-1)).strftime("%Y-%m-%d")
        TelegramNow = namedtuple('TelegramNow', 'index, date_telegrame, telegram', defaults=None)
        TelegramLast = namedtuple('TelegramLast', 'index, date_telegrame, telegram', defaults=None)
        if x.date_telegrame[0:10] == date_now:
            self.telegrame_now = TelegramNow(x.index, x.date_telegrame, x.telegram)
            yield self.telegrame_now
        if x.date_telegrame[0:10] == date_last:
            self.telegrame_last = TelegramLast(x.index, x.date_telegrame, x.telegram)
            yield self.telegrame_last

