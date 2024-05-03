from flask import Blueprint

from services.user import create_user_service, get_users_service

user = Blueprint('user', __name__)

@user.route('/', methods=['GET'])
def get_users():
  return get_users_service()

@user.route('/create', methods=['POST'])
def create_user():
  return create_user_service()