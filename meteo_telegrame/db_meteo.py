
import sqlite3 as sq

def index_meteo():
    with open('index_meteo.txt', 'r')as f:
        file = f.read()
        index_gagues = []
        for x in file.split():
            index_gagues.append(x)
        return index_gagues


def create_db_meteo():
    with sq.connect('../meteo_telegrame.db') as con:
        cur = con.cursor()
        cur.execute('''CREATE TABLE  index_meteo
                        (index_meteo TEXT )
                         ''')
        con.commit()
        for i in index_meteo():
            index_i = int(i)
            print(index_i)
            cur.execute(f'''CREATE TABLE  '{index_i}'
                   (date DATA,
                   meteo_telegrame TEXT)''')
            con.commit()



def save_db():
    with sq.connect('../meteo_telegrame.db') as con:
        cur = con.cursor()
        for i in index_meteo():
            data = i
            print(data)
            cur.execute(''' INSERT INTO index_meteo
                        (index_meteo)
                        VALUES(?)''', (data,))
            con.commit()

# create_db_meteo()
# save_db()