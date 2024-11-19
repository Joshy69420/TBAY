import requests 
import sqlite3
user_league=input("enter a league")
user_country=input("enter a country")
# define connection to league table and create cursor
connection= sqlite3.connect("tbay.db")

cursor=connection.cursor()


query=  f"SELECT id FROM leagues WHERE name ='{user_league}' AND country ='{user_country}'"
cursor.execute(query)
columns=cursor.fetchall()[0]

for column in columns:
    print(column)