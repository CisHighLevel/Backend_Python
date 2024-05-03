from flask import request, Response
from bson import json_util, objectid

from config.mongodb import mongo

from models.User.model import User

def create_user_service():
    try:
        data = request.get_json()
        user_name = data.get('userName', None)
        mail = data.get('mail', None)
        password = data.get('password', None)
        
        if user_name and mail and password:
            print(user_name, mail, password)
            new_user = User(user_name=user_name, mail=mail, password=password)
            print(new_user)
            mongo.db.users.insert_one(new_user.to_dict())  # Guardar el nuevo usuario en MongoDB
            return 'User created successfully', 201
        else:
            return 'Invalid payload', 400
    except Exception as e:
        print(e)

def get_users_service():
    users = mongo.db.users.find()
    result = json_util.dumps(users)
    return Response(result, mimetype='application/json')
    
def get_users_service():
    data = mongo.db.User.find()
    result = json_util.dumps(data)
    return Response(result, mimetype='application/json')

