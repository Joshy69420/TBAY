import requests 
import sqlite3 



headers = {
    "x-apisports-key": "6732a3d212744481c28f836db783c293"
}

# Endpoint to get all leagues
url = "https://v3.football.api-sports.io/leagues"

response = requests.get(url, headers=headers)
data = response.json()

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect("tbay.db")
cursor = conn.cursor()

# Create a table for leagues
cursor.execute(""" CREATE TABLE IF NOT EXISTS leagues (id INTEGER PRIMARY KEY,name TEXT,country TEXT)""")

# Insert league IDs names and countries into the table
for league in data["response"]:
    league_id = league["league"]["id"]
    league_name = league["league"]["name"]
    league_country= league["country"]["name"]
    cursor.execute("INSERT OR IGNORE INTO leagues (id, name,country) VALUES (?, ?,?)", (league_id, league_name,league_country,))

# Commit changes and close the connection
conn.commit()
conn.close()

print("League info saved to tbay ")