#imports
from flask import Flask , render_template 
import sqlite3
import requests
leagues_list=[]
index=0
country_list=[]
global cursor

#retrieve leagues 
# define connection to tbay database and create cursor
connection= sqlite3.connect("tbay.db",check_same_thread=False)
cursor=connection.cursor()
query=  f"SELECT name FROM leagues"
cursor.execute(query)
columns=cursor.fetchall()
for column in columns:
    leagues_list.append(column[0])
#create subroutine to get league ids 
def get_id(league_name):
    query=f"SELECT id FROM leagues WHERE name ='{league_name}'"
    cursor.execute(query)
    columns=cursor.fetchall()
    return columns
#create subroutine to get all teams fom that league
def get_teams(league_id):
    headers = { "x-apisports-key": "6732a3d212744481c28f836db783c293"}
    url = "https://v3.football.api-sports.io/{{league_id}}&season={2022}"
    response = requests.get(url, headers=headers)
    data = response.json()
    print(data)
#run web application instance
app=Flask(__name__)
#define what the name of the page is 
@app.route("/search")
def search():
    return render_template ("stuff i need.html",leagues_list=leagues_list)
@app.route("/league_<league_name>")
def league_page(league_name):
    league_id=get_id(league_name)
    get_teams(league_id)
    return render_template("league page.html",league_name=league_name)

    
if __name__=='__main__': 
    app.run()