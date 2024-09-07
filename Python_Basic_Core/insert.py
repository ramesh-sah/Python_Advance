import sqlite3 
conn =sqlite3.connect("sqlite.db")
ins = '''
    insert into students( st_name,st_class,st_email) 
    values('ram','11th','ram@gmail.com')
'''
conn.execute(ins)
conn.commit()
conn.close()