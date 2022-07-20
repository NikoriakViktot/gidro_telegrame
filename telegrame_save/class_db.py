import sqlite3
import datetime

class Database:


    def __init__(self, **kwargs):
        self.filename = kwargs.get('filename')
        self.table = kwargs.get('table')


    def database_query(self, query, *params):
        self._db.execute(query, params)
        self._db.commit()

    def insert_dict(self,qwery, **kwargs):
        column = qwery
        # value=tuple([x.replace(x, '?') for x in column.split(',')])
        row = tuple(kwargs.values())
        self._db.execute(column, row)
        self._db.commit()

    # def select_telegram_date(self, key):
    #     query= 'SELECT gauges_telegrame FROM {} WHERE'.format(self._table)
    #
    #     '{int(self.index)}'
    #     WHERE
    #     date = '{(datetime.datetime.today() + datetime.timedelta(days=-1)).strftime
    #     ("%Y-%m-%d")} 0
    #     8: 00:00
    #     ' '''
    #     date_last = (datetime.datetime.today() + datetime.timedelta(days=-1)).strftime("%Y-%m-%d")
    #     cursor = self._db.execute('select * from {} where '' = ?'.format(self._table), (key,))
    #     return dict(cursor.fetchone())

    def select_date_now(self, key):
        date_now = datetime.date.today().strftime("%Y-%m-%d")
        cursor = self._db.execute('select * from {} where '' = ?'.format(self._table), (key,))
        return dict(cursor.fetchone())


    def select_date(self,index, date=0):
        date_select = (datetime.datetime.today() + datetime.timedelta(days=date)).strftime("%Y-%m-%d")
        qwery_date = 'SELECT gauges_telegrame FROM gidro_telegram WHERE ' \
                     'index_hydro_station={} AND date = "{} 08:00:00"'.format(int(index),date_select)
        cursor = self._db.execute(qwery_date)
        return cursor.fetchone()

    def update(self,index,*data,date=0):
        date_select = (datetime.datetime.today() + datetime.timedelta(days=date)).strftime("%Y-%m-%d")
        qwery ='update {} set gauges_telegrame = ?' \
               ' where index_hydro_station={} AND' \
               ' date = "{} 08:00:00"'' = ?'.format(self._table,int(index),date_select)
        self._db.execute(qwery, data)
        self._db.commit()

    def delete(self,query,key):
        query = query
        self._db.execute(query,(key,))
        self._db.commit()

    def disp_rows(self):
        cursor = self._db.execute('select * from {} order by '' '.format(self._table))
        for row in cursor:
            print('  {}: {}'.format(row[' '], row[' ']))

    def __iter__(self,*args):
        cursor = self._db.execute('select * from {}  '.format(self._table))
        for row in cursor:
            yield row


    @property
    def filename(self): return self._filename

    @filename.setter
    def filename(self, fn):
        self._filename = fn
        self._db = sqlite3.connect(fn)
        self._db.row_factory = sqlite3.Row

    @filename.deleter
    def filename(self): self.close()

    @property
    def table(self): return self._table

    @table.setter
    def table(self, t): self._table = t

    @table.deleter
    def table(self): self._table = 'test'

    def close(self):
            self._db.close()
            del self._filename






if __name__ == '__main__':
    file = '../gauges_telegrame1.db'
    d = Database(filename=file, table='index_gauges')
    d.database_query('drop table if exists index_gauges')
    d.database_query('CREATE TABLE IF NOT EXISTS  index_gauges (index_gauges TEXT NOT NULL)')
    #
    def index_gagues():
        with open('index.txt', 'r') as f:
            file = f.read()
            index_gagues = []
            for x in file.split():
                index_gagues.append(x)
            return index_gagues

    for i in index_gagues():
        data = i
        query = "INSERT INTO  index_gauges(index_gauges) VALUES(?)"
        d.database_query(query,data)

    # for row in d:
    #     print(dict(row))

    query_telegram = 'CREATE TABLE IF NOT EXISTS gidro_telegram' \
                     ' (index_hydro_station INTEGER,' \
                     ' date TEXT, gauges_telegrame TEXT)'
    telegram_tabl = Database(filename=file)
    telegram_tabl.database_query(query_telegram)






    #     def create_db(self):
    #         with sq.connect('../gauges_telegrame.db') as con:
    #             cur = con.cursor()
    #             cur.execute('''CREATE TABLE  index_gauges
    #                             (index_gauges TEXT NOT NULL)
    #                              ''')
    #             con.commit()
    #             for i in self.index_gagues():
    #                 index_i = int(i)
    #                 # print(index_i)
    #                 cur.execute(f'''CREATE TABLE  '{index_i}'
    #                        (date TEXT,
    #                        gauges_telegrame TEXT NOT NULL)''')
    #                 con.commit()
    #
    #
    #     def save_db(self):
    #         with sq.connect('../gauges_telegrame.db') as con:
    #             cur = con.cursor()
    #             for i in self.index_gagues():
    #                 data = i
    #                 cur.execute(''' INSERT INTO index_gauges
    #                             (index_gauges)
    #                             VALUES(?)''', (data,))
    #                 con.commit()
    #
    #
    #     def request_index(self):
    #         with sq.connect('../gauges_telegrame.db') as con:
    #             cur = con.cursor()
    #             cur.execute("SELECT * FROM index_gauges")
    #             index = [x[0] for x in cur.fetchall()]
    #             for value in index:
    #                 INDEX = []
    #                 INDEX.append(value)
    #                 yield INDEX

    # print(d.__dir__())
    # print(list(d.__iter__()))

    # d = Data_Base()
    #
    # d.db.connect()
    # create_db()
    # save_db()
