from flask import request, Response
from bson import json_util, ObjectId
from services.data import create_data_service

from config.mongodb import mongo

def create_humidity_service():
    try:
        value = create_data_service(request.get_json())
        if value:
            mongo.db.humidities.insert_one(value.to_dict())  # Guardar el nuevo usuario en MongoDB
            return 'humidity created successfully', 201
        else:
            return 'Invalid payload', 400
    except Exception as e:
        print(e)
    

def get_humidities_service():
    humidity = mongo.db.humidities.find()
    result = json_util.dumps(humidity)
    return Response(result, mimetype='application/json')

def get_humidity_service(id):
    humidity = mongo.db.humidities.find_one({'_id': ObjectId(id)})
    result = json_util.dumps(humidity)
    return Response(result, mimetype='application/json')

def update_humidity_service(id):
    humidity = request.get_json()
    if len(humidity) == 0:
      return 'Invalid payload', 400
    
    response = mongo.db.humidities.update_one({'_id': ObjectId(id)}, {'$set': humidity})

    if response.modified_count >= 1:
        return 'humidity updated successfully', 200
    else:
        return 'humidity not found', 404

def delete_humidity_service(id):
    response = mongo.db.humidities.delete_one({'_id': ObjectId(id)})
    if response.deleted_count >= 1:
        return 'humidity deleted successfully', 200
    else:
        return 'humidity not found', 404