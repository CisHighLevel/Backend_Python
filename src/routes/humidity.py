from flask import Blueprint

from services.humidity import create_humidity_service, get_humidities_service, get_humidity_service, update_humidity_service, delete_humidity_service, get_latest_humidity_service

humidity = Blueprint('humidity', __name__)

@humidity.route('/', methods=['GET'])
def get_humidities():
  return get_humidities_service()

@humidity.route('/<id>', methods=['GET'])
def get_humidity(id):
  return get_humidity_service(id)

@humidity.route('/create', methods=['POST'])
def create_humidity():
  return create_humidity_service()

@humidity.route('/<id>', methods=['PUT'])
def update_humidity(id):
  return update_humidity_service(id)

@humidity.route('/<id>', methods=['DELETE'])
def delete_humidity(id):
  return delete_humidity_service(id)

@humidity.route('/latest', methods=['GET'])
def get_latest_humidity():
    return get_latest_humidity_service()
