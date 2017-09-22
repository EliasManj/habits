import sqlite3

connection = sqlite3.connect("data.db")
cursor = connection.cursor()

query = "CREATE TABLE IF NOT EXISTS habitList (id INTEGER PRIMARY KEY, habit TEXT, times INTEGER, color TEXT, description TEXT, initDate date)"

cursor.execute(query)

insertQuery = "INSERT INTO habitList VALUES (NULL, ?, ?, ?, ?, ?)"
habitData = [
    ("drink_water", 1, " #3498db", "drink lots of water", "2017-09-21"),
    ("put_lotion", 2, "#f0b27a", "for the hair", "2017-09-21"),
    ("read_book", 1, " #d2b4de", "in the night", "2017-09-21"),
    ("stretch", 2, "#e67e22", "in the night", "2017-09-21")
]

cursor.executemany(insertQuery, habitData)  

createDatesQuery = "CREATE TABLE IF NOT EXISTS datesTable(id INTEGER PRIMARY KEY, currentDate date)"
cursor.execute(createDatesQuery)
dates = [
    ('2017-09-15',),
    ('2017-09-16',),
    ('2017-09-17',),
    ('2017-09-18',),
    ('2017-09-19',),
    ('2017-09-20',),
    ('2017-09-21',)
]
insertDates = "INSERT INTO datesTable VALUES (NULL,?)"
cursor.executemany(insertDates, dates)

for habit in habitData:
    actQuery = "ALTER TABLE datesTable ADD COLUMN {0} INT NOT NULL DEFAULT 0".format(habit[0])
    cursor.execute(actQuery)

connection.commit()
connection.close()
