from flask_restful import Resource, reqparse
from models.habit import HabitModel
import datetime

class Msg():

    @classmethod
    def showMsg(seld, text):
        return {'message': text}

class HabitList(Resource):

    def get(self):
        habitList = HabitModel.findAll()
        if habitList:
            return {'habits' : habitList}, 200
        else:
            return showMsg("there are no habits yet"), 404

class Habit(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('name', type=str, required=True, help="This field is required")
    parser.add_argument('times', type=int, required=True, help="This field is requires")
    parser.add_argument('color', type=str, required=True, help="This field is requires")
    parser.add_argument('desc', type=str, required=True, help="This field is requires")

    def get(self, name):
        habit = HabitModel.findByHabit("_".join(name.split("+")).lower())
        if habit:
            return {'habit': habit.getName(), 'times': habit.getTimes(), 'color': habit.getColor(), 'desc': habit.getDesc(), 'created in': habit.getInitDate()}
        else:
            return Msg.showMsg("habit not found"), 404

    def post(self, name):
        requestData = Habit.parser.parse_args()
        if HabitModel.findByHabit("_".join(requestData['name'].split(" ")).lower()):
            return Msg.showMsg("There already exists a habit with that name")
        today = datetime.date.today()
        newHabit = HabitModel(requestData['name'], requestData['times'], requestData['color'], requestData['desc'], str(today))
        result = newHabit.insert()
        if result:
            return Msg.showMsg('habit added')
        else:
            return Msg.showMsg("something happened..."), 500
