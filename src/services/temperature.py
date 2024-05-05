from flask import request, Response
from bson import json_util, ObjectId
from services.data import create_data_service

from config.mongodb import mongo

def create_temperature_service():
    try:
        value = create_data_service(request.get_json())
        if value:
            mongo.db.temperatures.insert_one(value.to_dict())  # Guardar el nuevo usuario en MongoDB
            return 'temperature created successfully', 201
        else:
            return 'Invalid payload', 400
    except Exception as e:
        print(e)
    

def get_temperatures_service():
    temperature = mongo.db.temperatures.find()
    result = json_util.dumps(temperature)
    return Response(result, mimetype='application/json')

def get_temperature_service(id):
    temperature = mongo.db.temperatures.find_one({'_id': ObjectId(id)})
    result = json_util.dumps(temperature)
    return Response(result, mimetype='application/json')

def update_temperature_service(id):
    temperature = request.get_json()
    if len(temperature) == 0:
      return 'Invalid payload', 400
    
    response = mongo.db.temperatures.update_one({'_id': ObjectId(id)}, {'$set': temperature})

    if response.modified_count >= 1:
        return 'temperature updated successfully', 200
    else:
        return 'temperature not found', 404

def delete_temperature_service(id):
    response = mongo.db.temperatures.delete_one({'_id': ObjectId(id)})
    if response.deleted_count >= 1:
        return 'temperature deleted successfully', 200
    else:
        return 'litemperatureght not found', 404
    
def get_latest_temperature_service():
    data = mongo.db.temperatures.find().sort([('_id', -1)]).limit(1)
    latest_data = next(data, None)  # Extraer el primer documento del cursor
    if latest_data:
        # Obtener el valor 'value' del documento
        latest_value = latest_data.get('value')
        # Convertir el valor a JSON
        result = json_util.dumps({'value': latest_value})
        return Response(result, mimetype='application/json')
    else:
        # Si no hay datos, devolver un objeto JSON vacío
        return Response({}, mimetype='application/json')    