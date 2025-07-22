import sqlite3
conn=sqlite3.connect("mydata.db")
cursor=conn.cursor()
cursor.execute("INSERT INTO USER (name,age) VALUES(?,?)",("alice", 25))
cursor.execute("INSERT INTO USER (name,age) VALUES(?,?)",("bob", 35))
conn.commit()
conn.close()
