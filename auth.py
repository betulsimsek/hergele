from flask import Flask, request, jsonify
import os
from pymongo import MongoClient
from dotenv import load_dotenv


users = []
load_dotenv()

# Get MongoDB URI and DB name from environment variables
mongodb_uri = os.getenv("MONGODB_URI")
db_name = os.getenv("DB_NAME")

# Connect to MongoDB
client = MongoClient(mongodb_uri)
db = client[db_name]
collection = db['users']


app = Flask(__name__)
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/authenticate', methods=['POST'])
def authenticate():
    # Get the headers from the request
    headers = request.headers
    
    # Get the values from the headers
    filo = headers.get('Filo')
    authorization = headers.get('Authorization')
    user_no = headers.get('userNo')
    user = db['users'].find_one({'userNo': user_no})
    authorization_code = request.args.get('authorizationCode')

    # Perform authentication and return the result as a response
    if filo == 'hergele' and authorization == authorization_code and user_no == user:
        response = {'message': 'Kullanıcı doğrulandı.'}
    else:
        response = {'message': 'Kullanıcı doğrulanamadı.'}

    db['auth_responses'].insert_one(response)
    
    return jsonify(response)

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
    app.run(debug=True)

