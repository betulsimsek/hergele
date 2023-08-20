from flask import jsonify

def handle_error(error_message, status_code):
    response = jsonify({'error': error_message})
    return response, status_code
