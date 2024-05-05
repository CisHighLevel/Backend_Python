from flask import request, Response
from bson import json_util, ObjectId
from services.data import create_data_service

from config.mongodb import mongo

def create_light_service():
    try:
        value = create_data_service(request.get_json())
        if value:
            mongo.db.lights.insert_one(value.to_dict())  # Guardar el nuevo usuario en MongoDB
            return 'light created successfully', 201
        else:
            return 'Invalid payload', 400
    except Exception as e:
        print(e)
    

def get_lights_service():
    light = mongo.db.lights.find()
    result = json_util.dumps(light)
    return Response(result, mimetype='application/json')

def get_light_service(id):
    light = mongo.db.lights.find_one({'_id': ObjectId(id)})
    result = json_util.dumps(light)
    return Response(result, mimetype='application/json')

def update_light_service(id):
    light = request.get_json()
    if len(light) == 0:
      return 'Invalid payload', 400
    
    response = mongo.db.lights.update_one({'_id': ObjectId(id)}, {'$set': light})

    if response.modified_count >= 1:
        return 'light updated successfully', 200
    else:
        return 'light not found', 404

def delete_light_service(id):
    response = mongo.db.lights.delete_one({'_id': ObjectId(id)})
    if response.deleted_count >= 1:
        return 'light deleted successfully', 200
    else:
        return 'light not found', 404