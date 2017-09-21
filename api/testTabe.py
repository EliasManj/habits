import sqlite3

connection = sqlite3.connect("data.db")
cursor = connection.cursor()

query = "CREATE TABLE IF NOT EXISTS habitList (id INTEGER PRIMARY KEY, habit TEXT, times INTEGER, color TEXT, description TEXT)"
