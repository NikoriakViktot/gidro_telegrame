import sqlite3

class Database:


    def __init__(self, **kwargs):
        self.filename = kwargs.get('filename')
        self.table = kwargs.get('table')


    def sql_do(self, sql, *params):
        self._db.execute(sql, params)
        self._db.commit()

    def insert(self,*args, **kwargs):
        column = args[0]
        # value=tuple([x.replace(x, '?') for x in column.split(',')])
        row = tuple(kwargs.values())
        self._db.execute(column, row)
        self._db.commit()

    def retrieve(self, key):
        cursor = self._db.execute('select * from {} where '' = ?'.format(self._table), (key,))
        return dict(cursor.fetchone())

    def update(self, row):
        self._db.execute(
            'update {} set '' = ? where '' = ?'.format(self._table),
            (row[''], row['']))
        self._db.commit()

    def delete(self, key):
        self._db.execute('delete from {} where '' = ?'.format(self._table), (key,))
        self._db.commit()

    def disp_rows(self):
        cursor = self._db.execute('select * from {} order by '' '.format(self._table))
        for row in cursor:
            print('  {}: {}'.format(row[' '], row[' ']))

    def __iter__(self,*args):
        cursor = self._db.execute('select * from {}  '.format(self._table))
        for row in cursor:
            yield dict(row)

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




# class Data_Base(object):
#
#
#     def __init__(self, path_db, data):
#         self.data = data
#         self.requst_db = requst_db
#
#     def index_gagues(self):
#         with open('index.txt', 'r') as f:
#             file = f.read()
#             index_gagues = []
#             for x in file.split():
#                 index_gagues.append(x)
#             return index_gagues
#
#
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


if __name__ == '__main__':
    d = Database(filename='gauges1.db', table='index_gauges')
    # d.sql_do('drop table if exists index_gauges')
    # d.sql_do('CREATE TABLE IF NOT EXISTS  index_gauges (index_gauges TEXT NOT NULL)')
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
        dd = dict(index_gauges=data)

        args = ("INSERT INTO  index_gauges(index_gauges) VALUES(?)",)
        d.insert(*args,**dd)
        d.close()
    for row in d:
        print(row.items())


    # d.close()







    # print(d.__dir__())
    # print(list(d.__iter__()))

    # d = Data_Base()
    #
    # d.db.connect()
    # create_db()
    # save_db()
