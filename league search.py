import requests 
import sqlite3
user_league=input("enter a league")

# define connection to league table and create cursor
connection= sqlite3.connect("leagues.db")

cursor=connection.cursor()
#sigma
query=  "SELECT id FROM leagues WHERE name ='cup' "
cursor.execute(query)
columns=cursor.fetchall()

for column in columns:
    print(column)