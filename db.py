
import sqlite3 as sq

def index_gagues():
    with open('index.txt', 'r')as f:
        file = f.read()
        index_gagues = []
        for x in file.split():
            index_gagues.append(x)
        return index_gagues


def create_db():
    with sq.connect('gauges_telegrame.db') as con:
        cur = con.cursor()
        cur.execute('''CREATE TABLE  index_gauges
                        (index_gauges TEXT NOT NULL)
                         ''')
        con.commit()
        for i in index_gagues():
            index_i = int(i)
            # print(index_i)
            cur.execute(f'''CREATE TABLE  '{index_i}'
                   (date DATA,
                   gauges_telegrame TEXT NOT NULL)''')
            con.commit()



def save_db():
    with sq.connect('gauges_telegrame.db') as con:
        cur = con.cursor()
        for i in index_gagues():
            data = i
            cur.execute(''' INSERT INTO index_gauges
                        (index_gauges)
                        VALUES(?)''', (data,))
            con.commit()




