import sqlite3

class HabitModel():

    def __init__(self, name, times, color, desc):
        self.name = name
        self.times = times
        self.color = color
        self.desc = desc

    def getName(self):
        return self.name

    def getTimes(self):
        return self.times

    def getColor(self):
        return self.color

    def getDesc(self):
        return self.desc

    @classmethod
    def findByHabit(cls, name):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = "SELECT * FROM habitList WHERE habit=?"
        queryResult = cursor.execute(query, (name,))
        result = queryResult.fetchone()
        connection.commit()
        connection.close()
        print(result)
        if result:
            return cls(result[1], result[2], result[3], result[4])
