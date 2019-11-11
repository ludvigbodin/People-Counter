from flask import Flask
from flask_restful import Api
from flask_cors import CORS
import _thread

from resources.count import Count
from resources.stats import Stats

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'

api = Api(app)

api.add_resource(Count, "/count")
api.add_resource(Stats, "/stats")

if __name__ == '__main__':
    app.run()
    