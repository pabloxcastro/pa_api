from flask import Flask
from flask_restful import Api
from src.controllers.publication import Publication
from src.config.config import *
 
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{user}:{pwd}@{host}:5432/{database}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)

@app.before_first_request
def create_db():
    banco.create_all()

api.add_resource(Publication, '/publications')

@app.route('/')
def home():
   return "API on line"

if __name__ == '__main__':
    from sql_alchemy import banco
    banco.init_app(app)
    app.run(host="0.0.0.0", port=int("8080"), debug=True)
