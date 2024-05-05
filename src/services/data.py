from flask import request, Response
from bson import json_util, ObjectId
import datetime

from config.mongodb import mongo

from models.Data.model import Data

def create_data_service(data):
    try:
        data = request.get_json()
        print(data)
        time = datetime.datetime.now()
        value = data.get('value', None)
        if time:
            return Data(time=time, value=value,)
        else:
            return 'error'
    except Exception as e:
        print(e)