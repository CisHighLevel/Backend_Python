from flask import Blueprint

from services.data import create_data_service, get_datas_service, get_data_service, update_data_service, delete_data_service

data = Blueprint('data', __name__)

@data.route('/', methods=['GET'])
def get_datas():
  return get_datas_service()

@data.route('/<id>', methods=['GET'])
def get_data(id):
  return get_data_service(id)

@data.route('/create', methods=['POST'])
def create_data():
  return create_data_service()

@data.route('/<id>', methods=['PUT'])
def update_data(id):
  return update_data_service(id)

@data.route('/<id>', methods=['DELETE'])
def delete_data(id):
  return delete_data_service(id)
