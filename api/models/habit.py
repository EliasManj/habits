import sqlite3


class HabitModel():

    def __init__(self, name, times, color, desc, initDate):
        self.name = name
        self.times = times
        self.color = color
        self.desc = desc
        self.initDate = initDate

    def getName(self):
        return self.name

    def getTimes(self):
        return self.times

    def getColor(self):
        return self.color

    def getDesc(self):
        return self.desc

    def getInitDate(self):
        return self.initDate

    @classmethod
    def findByHabit(cls, name):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = "SELECT * FROM habitList WHERE habit=?"
        queryResult = cursor.execute(query, (name,))
        result = queryResult.fetchone()
        if result is None:
            return None
        result = result[1:]
        return cls(*result)
        connection.commit()
        connection.close()

    @classmethod
    def findAll(cls):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = "SELECT * FROM habitList"
        queryResult = cursor.execute(query)
        result = list(queryResult)
        result = [x[1:] for x in result]
        if result:
            return result
        connection.commit()
        connection.close()

    def insert(self):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = "INSERT INTO habitList VALUES (NULL, ?, ?, ?, ?, ?)"
        try:
            cursor.execute(query, (self.getName(), self.getTimes(), self.getColor(), self.getDesc(), self.getInitDate()))
        except:
            return None
        connection.commit()
        connection.close()
        return self
