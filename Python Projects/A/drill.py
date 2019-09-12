import sqlite3
import os

con = sqlite3.connect('dbType.db')

with con:
    cur = con.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS tbl_ext( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_dataType TEXT)')
    con.commit()

fPath = 'C:\\Users\\Tyler\\Desktop\\Coding\\Python\\Python Projects\\sql_drill\\'
pathList = os.listdir(fPath)

con = sqlite3.connect('dbType.db')

with con:
    cur = con.cursor()
    for i in pathList:
        if i.endswith('.txt'):
            cur.execute('INSERT INTO tbl_ext(col_dataType) VALUES (?)', (i,))
    con.commit()

with con:
    cur = con.cursor()
    cur.execute('SELECT col_dataType FROM tbl_ext')
    for file in cur:
        print(file)
con.close()
    



    
