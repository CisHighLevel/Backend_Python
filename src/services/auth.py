from flask import Flask, request, jsonify
from flask_bcrypt import Bcrypt
import os
from config.mongodb import mongo
import jwt

from models.User.model import User

auth = Flask(__name__)
auth.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
bcrypt = Bcrypt(auth)

def login():
    try:
        data = request.get_json()
        mail = data.get('mail', None)
        password = data.get('password', None)

        if mail and password:
            user = mongo.db.users.find_one({'mail': mail})
            if user and bcrypt.check_password_hash(user['password'], password):
                session = {"id": mail}
                token = jwt.encode(session, 'SECRET_KEY', algorithm="HS256")

                print(f"Generated token: {token}")

                return jsonify({'message': 'Login successful:', 'token': token}), 200
            else:
                return jsonify({'message': 'Invalid mail or password'}), 401
        else:
            return jsonify({'message': 'Invalid payload'}), 400
    except Exception as e:
        return jsonify({'message': str(e)}), 500

# if __name__ == '__main__':
#     auth.run(debug=True)