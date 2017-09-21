import sqlite3

class HabitModel():

    def __init__(self, name, times, color):
        self.name = name
        self.times = times
        self.color = color

    @classmethod
    def findByHabit(cls, name):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = "SELECT * FROM habitList WHERE name=?"
        queryResult = query.execute(query, name)
