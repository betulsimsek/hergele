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

if __name__ == '__main__':
    app.run()
