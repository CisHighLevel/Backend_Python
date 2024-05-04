from flask import request, Response
from bson import json_util, ObjectId
import bcrypt

from config.mongodb import mongo

from models.Data.model import Data

def create_data_service():
    try:
        data = request.get_json()
        print(data)
        string = data.get('string', None)
        value = data.get('value', None)
        
        if value:
            new_data = Data(string=string, value=value,)
            mongo.db.datas.insert_one(new_data.to_dict())  # Guardar el nuevo usuario en MongoDB
            return 'Data created successfully', 201
        else:
            return 'Invalid payload', 400
    except Exception as e:
        print(e)

def get_datas_service():
    data = mongo.db.datas.find()
    result = json_util.dumps(data)
    return Response(result, mimetype='application/json')

def get_data_service(id):
    data = mongo.db.datas.find_one({'_id': ObjectId(id)})
    result = json_util.dumps(data)
    return Response(result, mimetype='application/json')

def update_data_service(id):
    data = request.get_json()
    if len(data) == 0:
      return 'Invalid payload', 400
    
    response = mongo.db.datas.update_one({'_id': ObjectId(id)}, {'$set': data})

    if response.modified_count >= 1:
        return 'data updated successfully', 200
    else:
        return 'data not found', 404

def delete_data_service(id):
    response = mongo.db.datas.delete_one({'_id': ObjectId(id)})
    if response.deleted_count >= 1:
        return 'data deleted successfully', 200
    else:
        return 'data not found', 404