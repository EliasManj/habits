from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from resources.habit import Habit

app = Flask(__name__)
api = Api(app)

api.add_resource(Habit, "/habit/<string:name>")

if __name__ == "__main__":
    app.run(port = 5000, debug = True)
