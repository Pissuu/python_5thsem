import sqlite3
con=sqlite3.connect('mydata.sqlite')
cur=con.cursor()
cur.execute('DROP TABLE IF EXISTS student')
cur.execute('CREATE TABLE student(name TEXT,usn VARCHAR)')
cur.execute('INSERT INTO student VALUES(?,?)',('abc','123bg'))
cur.execute('SELECT * FROM student')
for i in cur:
    print(i)
cur.close()

