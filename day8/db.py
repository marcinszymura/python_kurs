# zapytania posgreSQL
import psycopg2

conn = psycopg2.connect(
    host='localhost',
    database='zawodnicy',
    user='postgres',
    password='qwe123'
)


cur = conn.cursor()
cur.execute('select * from zawodnicy')

wyniki = cur.fetchall()

print(wyniki)

for zawodnik in wyniki:
    print(zawodnik[1])


#insert

cur = conn.curson()
cur.execute('insert into ')
conn.commit