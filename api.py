from flask import Flask, jsonify, request
from schema import UserSchema
from operator_opt import perform_payment, process_refund

app = Flask(__name__)

users = []
user_schema = UserSchema()

@app.route('/kart-saklama', methods=['POST'])
def kart_saklama():
    user_data = request.get_json()
    errors = user_schema.validate(user_data)
    if errors:
        return jsonify({'error': errors}), 400

    user = user_schema.load(user_data)

    users.append(user)

    return jsonify({'message': 'Kart başarıyla saklandı'}), 201


import logging

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
