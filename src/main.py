"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User, Contact, Group
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/user', methods=['GET'])
def handle_hello():

    response_body = {
        "msg": "Hello, this is your GET /user response "
    }

    return jsonify(response_body), 200

# Get all contact
@app.route('/contact', methods=['GET'])
def get_contact():

    contacts = Contact.query.all()
    results = list(map(lambda item: item.serialize(),contacts))

    response_body = {
        "msg": "Hello, this is your GET /user response ",
        "contacts": results
    }

    return jsonify(response_body), 200

# Creat a new cotact
@app.route('/contact', methods=['POST'])
def creat_contact():

    id = request.json.get('id')
    name = request.json.get('full_name')
    email = request.json.get('email')
    address = request.json.get('address')
    phone = request.json.get('phone')
    
    contact = Contact()
    contact.id= id
    contact.full_name = name
    contact.email = email
    contact.address = address
    contact.phone = phone
    
    db.session.add(contact)   
    db.session.commit()
    # print(contact)

    return jsonify(contact.serialize()), 201

# @app.route('/contacts', methods=['POST'])
# def create_contact():    
#     name = request.json.get('name')    
#     email = request.json.get('email')    
#     phone = request.json.get('phone')
#     data = request.get_json()    
#     name = data['name']    
#     email = data['email']    
#     phone = data['phone']
#     contact = Contact()    
#     ontact.name = name    
#     contact.email = email    
#     contact.phone = phone
#     db.session.add(contact)    
#     db.session.commit()
#     return jsonify(contact.serialize()), 201

# Get all groups
@app.route('/group', methods=['GET'])
def get_group():

    group = Group.query.all()
    result=list(map(lambda item: item.serialize(),group))

    print(result)

    response_body = {
        "msg": "Hello, this is your GET /group response ",
        "groups": result
    }

    return jsonify(response_body), 200

# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
