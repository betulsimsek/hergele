import secrets
from flask import Flask, jsonify, request
from schema import UserSchema, CardRegistrationSchema
from marshmallow import ValidationError
from operator_opt import perform_payment, process_refund, card_listing, card_registration, update_balance_with_card
from pymongo import MongoClient
from dotenv import load_dotenv
import os

app = Flask(__name__)

users = []
user_schema = UserSchema()
card_registration_schema = CardRegistrationSchema()
load_dotenv()

# Get MongoDB URI and DB name from environment variables
mongodb_uri = os.getenv("MONGODB_URI")
db_name = os.getenv("DB_NAME")

# Connect to MongoDB
client = MongoClient(mongodb_uri)
db = client[db_name]
collection = db['users']

@app.route('/kart-saklama', methods=['POST'])
def kart_saklama():
    user = request.args.get('userNo')
    card = request.args.get('cardNo')
    
    response, status_code = card_registration(user, card)

    return jsonify(response), status_code

@app.route('/kart-saklamali-odeme', methods=['POST'])
def kart_saklamali_odeme():
    user_no = request.args.get('userNo')
    amount = request.args.get('amount')

    response, status_code = perform_payment(user_no, amount)

    return jsonify(response), status_code

@app.route('/iade', methods=['POST'])
def iade():
    user_no = request.args.get('userNo')

    response, status_code = process_refund(user_no)

    return jsonify(response), status_code

@app.route('/update_balance', methods=['POST'])
def update_balance():
    user_no = request.args.get('userNo')
    balance = request.args.get('balance')
    response, status_code = update_balance_with_card(user_no, balance)

    return jsonify(response), status_code

@app.route('/kart-saklama-listesi', methods=['GET'])
def kart_saklama_listesi():
    user_no = request.args.get('userNo')

    # Use find_one to find a single document matching the user_no
    user = collection.find_one({'userNo': user_no})

    if user:
        cards = user['allCards']
    else:
        cards = []

    return jsonify({'cards': cards})


@app.route('/authenticate_first_route', methods=['POST'])
def authenticate_first_route():
    # Get the headers from the request
    headers = request.headers
    
    # Get the values from the headers
    filo = headers.get('Filo')
    user_no = headers.get('userNo')
    
    # Find the user document based on the userNo
    user = db['users'].find_one({'userNo': user_no})
    
    # Generate a new authorization code
    new_auth_code = secrets.token_hex(6)  # Generate a secure random hex token
    
    # Save the new authorization code in the auth collection for the user
    db['auth'].insert_one({'userNo': user_no, 'auth_code': new_auth_code})

    # Perform authentication and return the result as a response
    if filo == 'hergele' and user_no == user:
        response = {'message': 'User found.'}
        db['auth_responses'].insert_one(response)

    else:

        response = {'message': 'User not found.'}
        db['auth_responses'].insert_one(response)

    return jsonify({'message': 'Kullanıcı başarıyla bulundu.'}), 201


@app.route('/authenticate_second_route', methods=['POST'])
def authenticate_second_route():
    # Get the headers from the request
    headers = request.headers
    
    # Get the values from the headers
    filo = headers.get('Filo')
    authorization = headers.get('Authorization')
    user_no = headers.get('userNo')
    
    # Find the user document based on the userNo
    user = db['users'].find_one({'userNo': user_no})
    
    # Generate a new authorization code
    new_auth_code = secrets.token_hex(6)  # Generate a secure random hex token
    
    # Save the new authorization code in the auth collection for the user
    db['auth'].insert_one({'userNo': user_no, 'auth_code': new_auth_code})

    # Perform authentication and return the result as a response
    if filo == 'hergele' and authorization == new_auth_code and user_no == user:
        response = {'message': 'User verified.'}
    else:
        response = {'message': 'User authentication failed.'}

    db['auth_responses'].insert_one(response)
    
    return jsonify({'message': 'Kullanıcı başarıyla doğrulandı.'}), 201




@app.route('/create_user', methods=['POST'])
def create_user():
    data = request.get_json()
    
    user_no = data.get('userNo')
    auth_code = data.get('authCode')
    name = data.get('name')
    surname = data.get('surname')
    birth_date = data.get('birthDate')
    phone_number = data.get('phoneNumber')
    email = data.get('email')
    selected_card = data.get('selectedCard')
    all_cards = data.get('allCards')
    balance = data.get('balance')
    
    user = {
        'userNo': user_no,
        'authCode': auth_code,
        'name': name,
        'surname': surname,
        'birthDate': birth_date,
        'phoneNumber': phone_number,
        'email': email,
        'selectedCard': selected_card,
        'allCards': all_cards,
        'balance': balance
    }
    db['users'].insert_one(user)
    
    return jsonify({'message': 'Kullanıcı başarıyla oluşturuldu.'}), 201

if __name__ == '__main__':
    app.run()


