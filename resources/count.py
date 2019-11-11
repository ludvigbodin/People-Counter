from flask_restful import Resource
import json
from video.data import get_total_today, get_record_from_file

class Count(Resource):
    def get(self):
        inCount = 0
        outCount = 0
        
        total = get_total_today()
        record = get_record_from_file()
        print(record)

        return {"total": total, "record": record} 
    
    def post(self):
        print("Hello")