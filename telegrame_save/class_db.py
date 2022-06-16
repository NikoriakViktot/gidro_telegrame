import sqlite3 as sq


class Data_Base():
    db = sq

    # def __init__(self, requst_db, data):
    #     self.data = data
    #     self.requst_db = requst_db

    def index_gagues(self):
        with open('index.txt', 'r') as f:
            file = f.read()
            index_gagues = []
            for x in file.split():
                index_gagues.append(x)
            return index_gagues


    def create_db(self):
        with sq.connect('../gauges_telegrame.db') as con:
            cur = con.cursor()
            cur.execute('''CREATE TABLE  index_gauges
                            (index_gauges TEXT NOT NULL)
                             ''')
            con.commit()
            for i in self.index_gagues():
                index_i = int(i)
                # print(index_i)
                cur.execute(f'''CREATE TABLE  '{index_i}'
                       (date TEXT,
                       gauges_telegrame TEXT NOT NULL)''')
                con.commit()


    def save_db(self):
        with sq.connect('../gauges_telegrame.db') as con:
            cur = con.cursor()
            for i in self.index_gagues():
                data = i
                cur.execute(''' INSERT INTO index_gauges
                            (index_gauges)
                            VALUES(?)''', (data,))
                con.commit()


    def request_index(self):
        with sq.connect('../gauges_telegrame.db') as con:
            cur = con.cursor()
            cur.execute("SELECT * FROM index_gauges")
            index = [x[0] for x in cur.fetchall()]
            for value in index:
                INDEX = []
                INDEX.append(value)
                yield INDEX


if __name__ == '__main__':
    d = Data_Base()

    d.db.connect()
    # create_db()
    # save_db()
