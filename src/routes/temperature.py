from flask import Blueprint

from services.temperature import create_temperature_service, get_temperatures_service, get_temperature_service, update_temperature_service, delete_temperature_service, get_latest_temperature_service

temperature = Blueprint('temperature', __name__)

@temperature.route('/', methods=['GET'])
def get_temperatures():
  return get_temperatures_service()

@temperature.route('/<id>', methods=['GET'])
def get_temperature(id):
  return get_temperature_service(id)

@temperature.route('/create', methods=['POST'])
def create_temperature():
  return create_temperature_service()

@temperature.route('/<id>', methods=['PUT'])
def update_temperature(id):
  return update_temperature_service(id)

@temperature.route('/<id>', methods=['DELETE'])
def delete_temperature(id):
  return delete_temperature_service(id)

@temperature.route('/latest', methods=['GET'])
def get_latest_temperature():
    return get_latest_temperature_service()
