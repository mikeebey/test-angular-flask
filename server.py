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

class getBasicInfo(Resource):
    def get(self):
        return "Information"

api.add_resource(getBasicInfo,'/getbasicinfo')


if __name__ == '__main__':
    app.run(port=5002)
