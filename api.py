from flask import request, jsonify

from schema import UserSchema
from operator_opt import operator_opt, operator_iade


users = []
user_schema = UserSchema()


def kart_saklama():
    user_data = request.get_json()
    errors = user_schema.validate(user_data)
    if errors:
        return jsonify({'error': errors}), 400

    user = user_schema.load(user_data)

    users.append(user)

    return jsonify({'message': 'Kart başarıyla saklandı'}), 201


def kart_saklamali_odeme():
    user_no = request.json.get('userNo')
    amount = request.json.get('amount')

    for user in users:
        if user['userNo'] == user_no:
            if operator_opt(user_no, amount):
                user['balance'] -= amount
                return jsonify({'message': 'Ödeme başarıyla gerçekleştirildi'})
            else:
                return jsonify({'error': 'Ödeme işlemi gerçekleştirilemedi'}), 400

    return jsonify({'error': 'Kullanıcı bulunamadı'}), 404


def iade():
    user_no = request.json.get('userNo')
    amount = request.json.get('amount')

    for user in users:
        if user['userNo'] == user_no:
            if operator_iade(user_no, amount):
                user['balance'] += amount
                return jsonify({'message': 'İade başarıyla gerçekleştirildi'})
            else:
                return jsonify({'error': 'İade işlemi gerçekleştirilemedi'}), 400

    return jsonify({'error': 'Kullanıcı bulunamadı'}), 404


def kart_saklama_listesi():
    user_no = request.args.get('userNo')

    cards = []
    for user in users:
        if user['userNo'] == user_no:
            cards = user['allCards']
            break

    return jsonify({'cards': cards})
