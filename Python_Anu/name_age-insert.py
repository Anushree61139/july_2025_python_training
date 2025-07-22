import sqlite3
conn=sqlite3.connect("mydata.db")
cursor=conn.cursor()
name=input("enter the name")
age=int(input("enter the age"))
cursor.execute("insert into user(name,age)VALUES(?,?)",(name,age))
conn.commit()
conn.close()
