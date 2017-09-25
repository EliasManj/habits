from flask_restful import Resource, reqparse
from models.date import DateModel

class DateList(Resource):

    def get(self):
        dateList = DateModel.getAllDates()
        return {'dates': dateList}, 200
