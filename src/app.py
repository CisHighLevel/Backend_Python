from flask import Flask, render_template
from dotenv import load_dotenv
import os

from config.mongodb import mongo
from routes.user import user
from routes.data import data

config = load_dotenv()

app = Flask(__name__)

app.config['MONGO_URI'] = os.getenv('MONGO_URI')
mongo.init_app(app)

@app.route('/')
def index():
  return render_template('login.html')

app.register_blueprint(user, url_prefix='/user')
app.register_blueprint(data, url_prefix='/data')

if __name__ == '__main__':
  app.run(debug=True)