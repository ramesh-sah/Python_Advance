import sqlite3 
conn = sqlite3.connect("sqlite.db")
data = conn.execute("SELECT * FROM students limit 0,2")

for row in data:
    print(row)

conn.close()

