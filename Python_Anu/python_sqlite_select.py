import sqlite3
conn=sqlite3.connect("mydata.db")
cursor=conn.cursor()
cursor.execute("SELECT * FROM user")
rows = cursor.fetchall()
for row in rows:
    print(row)
conn.close()
