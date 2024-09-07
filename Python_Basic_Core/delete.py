import sqlite3
conn = sqlite3.connect("sqlite.db")
stu_name = input("Enter the student name:-")
conn.execute("select * from students where st_name="+stu_name)
conn.commit()
conn.close()  