import sqlite3 as sq


def request_index():
    with sq.connect('../gauges_telegrame.db') as con:
        cur = con.cursor()
        cur.execute("SELECT * FROM index_gauges")
        index = [x[0] for x in cur.fetchall()]
        for value in index:
            INDEX = []
            INDEX.append(value)
            yield INDEX






# print(open_html())
#
# for x in request_index():
#     print(x)