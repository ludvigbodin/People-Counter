from flask_restful import Resource
import json
from video.data import get_total_today

class Stats(Resource):
    def get(self):
        total = get_total_today()
        return {"total": total} 