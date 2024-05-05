from flask import Flask, render_template
from flask_cors import CORS
from dotenv import load_dotenv
import os

from config.mongodb import mongo
from routes.user import user
from routes.humidity import humidity
from routes.light import light
from routes.temperature import temperature

config = load_dotenv()

app = Flask(__name__)

# Configura CORS para permitir todas las solicitudes desde cualquier origen
CORS(app)

app.config['MONGO_URI'] = os.getenv('MONGO_URI')
mongo.init_app(app)

@app.route('/')
def index():
    return render_template('login.html')

app.register_blueprint(user, url_prefix='/user')
app.register_blueprint(humidity, url_prefix='/humidity')
app.register_blueprint(light, url_prefix='/light')
app.register_blueprint(temperature, url_prefix='/temperature')

if __name__ == '__main__':
  app.run(debug=True, host='10.192.230.83') # Reemplaza '192.168.1.100' con la dirección IP de tu ordenador

