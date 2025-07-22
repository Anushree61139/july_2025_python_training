import sqlite3
conn=sqlite3.connect("mydata.db")
cursor=conn.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS user(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email text not null,
    password text not null,
    age INTEGER
)
''')
conn.commit()
conn.close()
