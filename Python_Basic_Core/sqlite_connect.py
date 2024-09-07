import sqlite3 
conn = sqlite3.connect("sqlite.db")
create_table = ''' create table students (st_id INT Auto_increment  , st_name VARCHAR, st_class VARCHAR , st_email varchar)'''
conn.execute(create_table)
conn.close()