from flask import Blueprint

from api import iade, kart_saklamali_odeme, kart_saklama, update_balance, kart_saklama_listesi,  authenticate_first_route, create_user, authenticate_second_route

api_bp = Blueprint('api', __name__)

api_bp.add_url_rule('/kart-saklamali-odeme', 'kart_saklamali_odeme', kart_saklamali_odeme, methods=['PUT'])
api_bp.add_url_rule('/iade', 'iade', iade, methods=['PUT'])
api_bp.add_url_rule('/kart-saklama', 'kart-saklama', kart_saklama, methods=['POST'])
api_bp.add_url_rule('/update_balance', 'update_balance', update_balance, methods=['POST'])
api_bp.add_url_rule('/kart-saklama-listesi', 'kart-saklama-listesi', kart_saklama_listesi, methods=['GET'])
api_bp.add_url_rule('/create_user', 'create_user', create_user, methods=['POST'])
api_bp.add_url_rule('/authenticate_first_route', 'authenticate_first_route', authenticate_first_route, methods=['POST'])
api_bp.add_url_rule('/authenticate_second_route', 'authenticate_second_route', authenticate_second_route, methods=['POST'])



