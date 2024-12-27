import requests 
import sqlite3

# define connection to tbay database and create cursor
connection= sqlite3.connect("tbay.db")

cursor=connection.cursor()

cursor.execute("SELECT id FROM leagues order by id DESC LIMIT 1 ")
columns=cursor.fetchall()[0]
for column in columns:
    print(column)

