import sqlite3
global cursor
name=("ligma")
# Connect to SQLite database 
conn = sqlite3.connect("tbay.db")
cursor = conn.cursor()

query = "SELECT EXISTS(SELECT 1 FROM leagues WHERE name = ?)"
cursor.execute(query, (name,))
result = cursor.fetchone()
print(result[0])
