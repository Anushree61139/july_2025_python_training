import sqlite3
conn=sqlite3.connect("mydata.db")
cursor=conn.cursor()
Total=int(input("enter the Total number of students:"))
for i in range( Total):
    print(f"\n student {i+1}:")
    name=input("enter the name:")
    age=int(input("enter the age :"))
    cursor.execute("insert into user(name,age)VALUES(?,?)",(name,age))
conn.commit()
conn.close()