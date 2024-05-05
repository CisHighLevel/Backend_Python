from flask import Blueprint

from services.light import create_light_service, get_lights_service, get_light_service, update_light_service, delete_light_service

light = Blueprint('light', __name__)

@light.route('/', methods=['GET'])
def get_lights():
  return get_lights_service()

@light.route('/<id>', methods=['GET'])
def get_light(id):
  return get_light_service(id)

@light.route('/create', methods=['POST'])
def create_light():
  return create_light_service()

@light.route('/<id>', methods=['PUT'])
def update_light(id):
  return update_light_service(id)

@light.route('/<id>', methods=['DELETE'])
def delete_light(id):
  return delete_light_service(id)
