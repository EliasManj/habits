from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from resources.habit import Habit, HabitList
from resources.date import DateList

app = Flask(__name__)
api = Api(app)

api.add_resource(Habit, "/habit/<string:name>")
api.add_resource(HabitList, "/habits")
api.add_resource(DateList, "/habitdates")

if __name__ == "__main__":
    app.run(port = 5000, debug = True)
