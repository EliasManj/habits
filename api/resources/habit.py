from flask_restful import Resource, reqparse
from models.habit import HabitModel

class Msg():

    @classmethod
    def showMsg(seld, text):
        return {'message': text}

class Habit(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('name', type=str, required=True, help="This field is required")
    parser.add_argument('times', type=int, required=True, help="This field is requires")

    def get(self, name):
        habit = HabitModel.findByHabit("_".join(name.split("+")).lower())
        if habit:
            return {'habit': habit.getName(), 'times': habit.getTimes(), 'color': habit.getColor(), 'desc': habit.getDesc()}
        else:
            return Msg.showMsg("habit not found"), 404

    def post(self, name):
        requestData = Habit.parser.parse_args()
