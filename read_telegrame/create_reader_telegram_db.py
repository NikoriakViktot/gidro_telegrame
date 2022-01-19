
import sqlite3 as sq
from telegrame_save.request_index import request_index

def create_db_reader_telegram():
    with sq.connect('../reade_telegrame.db') as con:
        cur = con.cursor()
        for i in request_index():
            index_i = int(i[0])
            print(index_i)
            # cur.execute(f'''CREATE TABLE  '{index_i}'
            #        (date DATA,
            #        gauges_telegrame TEXT NOT NULL)''')
            # con.commit()





