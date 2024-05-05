from flask import request, Response
from bson import json_util, ObjectId
import bcrypt

from config.mongodb import mongo

from models.User.model import User

def create_user_service():
    try:
        data = request.get_json()
        print(data)
        user_name = data.get('user_name', None)
        mail = data.get('mail', None)
        password = data.get('password', None)
        
        if user_name:
            new_user = User(user_name=user_name, mail=mail, password=encryptPswd(password))
            mongo.db.users.insert_one(new_user.to_dict())  # Guardar el nuevo usuario en MongoDB
            return 'User created successfully', 201
        else:
            return 'Invalid payload', 400
    except Exception as e:
        print(e)

def get_users_service():
    print("grafana")
    users = mongo.db.users.find()
    result = json_util.dumps(users)
    return Response(result, mimetype='application/json')

def get_user_service(mail):
    data = mongo.db.users.find_one({'mail': mail})
    result = json_util.dumps(data)
    return Response(result, mimetype='application/json')

def update_user_service(id):
    data = request.get_json()
    if len(data) == 0:
      return 'Invalid payload', 400
    
    response = mongo.db.users.update_one({'_id': ObjectId(id)}, {'$set': data})

    if response.modified_count >= 1:
        return 'user updated successfully', 200
    else:
        return 'user not found', 404

def delete_user_service(id):
    response = mongo.db.users.delete_one({'_id': ObjectId(id)})
    if response.deleted_count >= 1:
        return 'user deleted successfully', 200
    else:
        return 'user not found', 404

def encryptPswd(password):
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password.encode("utf8"), salt)
        return hashed_password