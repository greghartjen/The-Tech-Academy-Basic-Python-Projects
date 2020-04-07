
import sqlite3
import os

conn = sqlite3.connect('drill.db')

with conn:
    cur = conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS tbl_file(\
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_filename TEXT \
        )')
    conn.commit()
conn.close()

conn = sqlite3.connect('drill.db')

with conn:
    cur = conn.cursor()
    cur.execute('INSERT INTO tbl_file(col_filename) VALUES (?)', \
                ('information.docx',))
    cur.execute('INSERT INTO tbl_file(col_filename) VALUES (?)', \
                ('Hello.txt',))
    cur.execute('INSERT INTO tbl_file(col_filename) VALUES (?)', \
                ('myImage.png',))
    cur.execute('INSERT INTO tbl_file(col_filename) VALUES (?)', \
                ('myMovie.mpg',))
    cur.execute('INSERT INTO tbl_file(col_filename) VALUES (?)', \
                ('World.txt',))
    cur.execute('INSERT INTO tbl_file(col_filename) VALUES (?)', \
                ('data.pdf',))
    cur.execute('INSERT INTO tbl_file(col_filename) VALUES (?)', \
                ('myPhoto.jpg',))
    conn.commit()
conn.close()

conn = sqlite3.connect('drill.db')

with conn:
    cur = conn.cursor()
    cur.execute('SELECT col_filename FROM tbl_file WHERE col_filename LIKE "%.txt%"')
    varFile = cur.fetchall()
    for items in varFile:
        message = "File name: {}".format(items)
        print(message)
conn.close()
    

