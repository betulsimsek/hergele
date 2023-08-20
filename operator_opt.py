from pymongo import MongoClient
from error_handler import handle_error
from error_messages import PAYMENT_ERROR_MESSAGES
from dotenv import load_dotenv
from pymongo import MongoClient
import os
from flask import jsonify


# .env dosyasından çevresel değişkenleri yükle
load_dotenv()

# MongoDB URI'sini ve veritabanı adını çevresel değişkenlerden al
mongodb_uri = os.getenv("MONGODB_URI")
db_name = os.getenv("DB_NAME")

# MongoDB'ye bağlan
client = MongoClient(mongodb_uri)
db = client[db_name]
collection = db['users']


def perform_payment(user_no, amount):
    user = collection.find_one({'userNo': user_no})

    if user and 'balance' in user:
        remaining_balance = user['balance'] - int(amount)

        if remaining_balance < 0:
            return PAYMENT_ERROR_MESSAGES['insufficient_balance'], 400
        # Bakiyeyi güncelle ve yeni ödeme işlemini geçmişe ekle
        collection.update_one(
            {'userNo': user_no},
            {
                '$set': {'balance': remaining_balance},
                '$push': {'transactions': {'type': 'payment', 'amount': int(amount)}}
            }
        )

        return {'message': 'Ödeme başarıyla gerçekleştirildi', 'balance': remaining_balance}, 201
    else:
        return PAYMENT_ERROR_MESSAGES['user_not_found_payment'], 400


def process_refund(user_no):
    user = collection.find_one({'userNo': user_no})

    if user and 'transactions' in user and len(user['transactions']) > 0:
        latest_payment = None

        # Geçmişteki en son ödeme işlemini bul
        for transaction in reversed(user['transactions']):
            if transaction['type'] == 'payment':
                latest_payment = transaction
                break

        if latest_payment and 'refund' not in latest_payment:
            amount = latest_payment['amount']
            remaining_balance = user['balance'] + amount

            if amount < 0:
                return PAYMENT_ERROR_MESSAGES['invalid_refund_amount'], 400

            # Bakiyeyi güncelle ve iade işlemini geçmişe ekle
            collection.update_one(
                {'userNo': user_no},
                {
                    '$set': {
                        'balance': remaining_balance
                    },
                    '$push': {
                        'transactions': {
                            'type': 'refund',
                            'amount': -amount,
                            'refund': True
                        }
                    }
                }
            )
            return {'message': 'İade başarıyla gerçekleştirildi', 'balance': remaining_balance}, 201
        else:
            return PAYMENT_ERROR_MESSAGES['refund_already_process'], 400
    else:
        return PAYMENT_ERROR_MESSAGES['user_not_found_refund'], 400


def card_listing(user_no):
    card_list = []

    user = collection.find_one({'userNo': user_no})

    if user.get('allCards'):
        for card in user['allCards']:
            card_list.append(card)
        return {'message': 'Kullanıcı kartları başarıyla listelendi', 'cards': card_list}, 200
    else:
        return PAYMENT_ERROR_MESSAGES['user_not_found_card_listing'], 400

    
def card_registration(user_no, card_no):
    user = collection.find_one({'userNo': user_no})

    if user and card_no:
        # Eğer kullanıcı koleksiyonda varsa
        if card_no in user['allCards']:
            return PAYMENT_ERROR_MESSAGES['card_number_already_exist'], 400
        elif len(card_no.replace(" ", "")) != 16:
            return PAYMENT_ERROR_MESSAGES['invalid_card_number'], 400
        else:
            collection.update_one(
                {'userNo': user_no},
                {
                    '$push': {'allCards': card_no}
                }
            )
            return {'message': 'Kart başarıyla saklandı'}, 201
    else:
        # Eğer kullanıcı koleksiyonda yoksa
        return PAYMENT_ERROR_MESSAGES['user_not_found_card_not_registration'], 400


    
def update_balance_with_card(user_no, balance):
    user = collection.find_one({'userNo': user_no})

    if user:
        # Kullanıcı bulundu, bakiyeyi güncelle
        old_balance = user['balance']
        new_balance = int(balance) + old_balance

        collection.update_one(
            {'_id': user['_id']},
            {'$set': {'balance': new_balance}}
        )
        
        return {'message': 'Bakiye başarıyla güncellendi'}, 201
    else:
        # Kullanıcı bulunamadı veya kart kayıt edilmedi
        return {'error': PAYMENT_ERROR_MESSAGES['user_not_found_card_not_registration']}, 404
