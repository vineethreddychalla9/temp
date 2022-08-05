import sqlite3
conn = sqlite3.connect('StudentInfo',timeout=2.0)
cur = conn.cursor()
cur.execute('DROP TABLE IF EXISTS Student')
cur.execute('CREATE TABLE Student (name TEXT,rno INTEGER)')
cur.execute('INSERT INTO Student VALUES(?,?)',('Mahesh',45))
cur.execute('INSERT INTO Student VALUES(?,?)',('Rahul',30))
data = cur.execute('SELECT * FROM Student')
print('Date in database is : ')
print(cur.fetchall())
conn.close()
'''
Output:
Date in database is:
('Mahesh', 45) ('Rahul', 30)
'''