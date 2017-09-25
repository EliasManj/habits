import sqlite3
import datetime

class DateModel:

    def __init__(year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def getAllDates():
        #Update table
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        lastDateQuery = "SELECT * FROM datesTable ORDER BY ID DESC LIMIT 1"
        lastDate = cursor.execute(lastDateQuery).fetchone()[1]
        todayObj = datetime.date.today()
        lastDateInt = list(map(int, lastDate.split('-')))
        lastDateObj = datetime.date(*lastDateInt)
        difference = (todayObj - lastDateObj).days
        dateListObj = [todayObj - datetime.timedelta(days=x) for x in range(0, difference)]
        dateList = list(map(str, dateListObj))[::-1]
        countColumns = "PRAGMA table_info(datesTable)"
        cols = cursor.execute(countColumns).fetchall()
        datesMat = list(map(lambda x : [x], dateList))
        for date in datesMat:
            date.extend(['0']*(len(cols)-2))
        datesTupleMap = list(map(lambda x: tuple(x), datesMat))
        insertNewDatesQuery = "INSERT INTO datesTable values (NULL{0})".format(",?"*(len(cols)-1))
        cursor.executemany(insertNewDatesQuery, datesTupleMap)
        #Fetch data
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        getAllDatesQuery = "SELECT * FROM datesTable"
        dates = cursor.execute(getAllDatesQuery).fetchall()
        connection.commit()
        connection.close()
        datesToList = list(map(lambda x: list(x), dates))
        colsToList = list(map(lambda x: list(x), cols))
        for date in datesToList:
            for j in range(2,len(colsToList)):
                date[j] = {colsToList[j][1]: date[j]}
        print(datesToList)
        return datesToList
