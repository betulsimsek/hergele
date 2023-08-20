from pymongo import MongoClient
from error_handler import handle_error
from error_messages import PAYMENT_ERROR_MESSAGES
from dotenv import load_dotenv
from pymongo import MongoClient
import os

# Load environment variables from .env
load_dotenv()

# Get MongoDB URI and DB name from environment variables
mongodb_uri = os.getenv("MONGODB_URI")
db_name = os.getenv("DB_NAME")

# Connect to MongoDB
client = MongoClient(mongodb_uri)
db = client[db_name]
collection = db['users']


def perform_payment(user_no, amount):
    user = collection.find_one({'userNo': user_no})

    if user and 'balance' in user:
        remaining_balance = user['balance'] - int(amount)

        if remaining_balance < 0:
            return handle_error(PAYMENT_ERROR_MESSAGES['insufficient_balance'], 400)

        # Update the balance and add the new payment transaction to the history
        collection.update_one(
            {'userNo': user_no},
            {
                '$set': {'balance': remaining_balance},
                '$push': {'transactions': {'type': 'payment', 'amount': int(amount)}}
            }
        )

        return {'message': 'Ödeme başarıyla gerçekleştirildi', 'balance': remaining_balance}, 201
    else:
        return handle_error(PAYMENT_ERROR_MESSAGES['user_not_found_payment'], 400)

def process_refund(user_no):
    user = collection.find_one({'userNo': user_no})

    if user and 'transactions' in user and len(user['transactions']) > 0:
        latest_payment = None

        # Find the latest payment transaction in the history
        for transaction in reversed(user['transactions']):
            if transaction['type'] == 'payment':
                latest_payment = transaction
                break

        if latest_payment:
            amount = latest_payment['amount']
            remaining_balance = user['balance'] + amount

            if amount < 0:
                return handle_error(PAYMENT_ERROR_MESSAGES['invalid_refund_amount'], 400)

            # Update the balance and add the refund transaction to the history
            collection.update_one(
                {'userNo': user_no},
                {
                    '$set': {'balance': remaining_balance},
                    '$push': {'transactions': {'type': 'refund', 'amount': -amount}}
                }
            )
            return {'message': 'İade başarıyla gerçekleştirildi', 'balance': remaining_balance}, 201
        else:
            return handle_error(PAYMENT_ERROR_MESSAGES['refund_payment_not_found'], 400)
    else:
        return handle_error(PAYMENT_ERROR_MESSAGES['user_not_found_refund'], 400)
