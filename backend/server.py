from flask import Flask,request
from flask_cors import CORS, cross_origin
from flask_restful import Resource,Api
from flask_jsonpify import jsonify
from json import dumps
import requests
import json
import csv
import ast
import math
import xml.etree.ElementTree as ET 


app = Flask(__name__)
api = Api(app)

CORS(app)
HOST = "0.0.0.0"
PORT = 5002
print("HERE")
class getBasicInfo(Resource):
    def get(self):
        return "Information"

class checkServer(Resource):
    def get(self):
        return "HEY I'm HERE"

api.add_resource(getBasicInfo,'/getbasicinfo')
api.add_resource(checkServer,'/')


if __name__ == '__main__':
    app.run(host=HOST,debug=True,port=PORT)
    #app.run(port=5002)
