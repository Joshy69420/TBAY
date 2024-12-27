import sqlite3
diddy=("diddy")
  # Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect("tbay.db")
cursor = conn.cursor()

# Create a table for leagues
cursor.execute(""" CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY,username TEXT,email TEXT,password TEXT)""")
is_found=(cursor.execute("SELECT id FROM users WHERE username= 'diddy'"))


