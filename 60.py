"""using sqlite library in python create a table employee with the attributes
employee_id, first_name, last_name, email, phone number, hire_date, job_id,
salary, manager_id, dept._id. Use insert command to insert the values of the
attributes in the employee table."""

import sqlite3
con=sqlite3.connect('mydata.sqlite')
cur=con.cursor()
cur.execute('DROP TABLE IF EXISTS employee')
cur.execute('CREATE TABLE employee(name TEXT,usn VARCHAR,employee_id PRIMARY KEY)')
cur.execute('INSERT INTO employee VALUES(?,?)',('abc','123bg'))
cur.commit()
cur.execute('SELECT * FROM employee')
for i in cur:
    print(i)
cur.close()

