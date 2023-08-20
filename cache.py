from flask import Flask, jsonify
import redis
import json

app = Flask(__name__)
r = redis.Redis()

@app.route('/users', methods=['GET'])
def get_users_from_cache():
    cache_key = 'users'

    # Önbellekteki veriyi kontrol edin
    data = r.get(cache_key)

    if data:
        # Eğer veri varsa, önbellekten okuyun ve sonucu döndürün
        users = json.loads(data)
        return jsonify(users)
    else:
        # Eğer veri yoksa, MongoDB sorgusunu gerçekleştirin
        users = User.find({})

        # Sorgu sonuçlarını JSON formatına dönüştürün
        users_json = json.dumps(users)

        # Sonuçları Redis'e önbelleğe yazın
        r.setex(cache_key, 3600, users_json) # Örnek olarak 1 saat süreyle önbelleğe alma

        return jsonify(users)

if __name__ == '__main__':
    app.run()
