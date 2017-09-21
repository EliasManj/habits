from flask_restful import Resource, reqparse

class Habit(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('name', type=str, required=True, help="This field is required")
    parser.add_argument('times', type=int, required=True, help="This field is requires")

    def get(self, name):
        return {'message':'ok'}

    def post(self, name):
        requestData = Habit.parser.parse_args()
        
