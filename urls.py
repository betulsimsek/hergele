from flask import Blueprint

from api import kart_saklama, kart_saklamali_odeme, iade, kart_saklama_listesi

api_bp = Blueprint('api', __name__)

api_bp.add_url_rule('/kart-saklama', 'kart_saklama', kart_saklama, methods=['POST'])
api_bp.add_url_rule('/kart-saklamali-odeme', 'kart_saklamali_odeme', kart_saklamali_odeme, methods=['PUT'])
api_bp.add_url_rule('/iade', 'iade', iade, methods=['PUT'])
api_bp.add_url_rule('/kart-saklama-listesi', 'kart_saklama_listesi', kart_saklama_listesi, methods=['GET'])
