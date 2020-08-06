from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

class allRequests(Resource):
    def get(self, name):
    def post(self, name):
    def put(self, name):
    def delete(self, name):

api.add_resource(allRequests, "/user/<string:name>")
