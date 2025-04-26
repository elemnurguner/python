
from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/')
def index():
    # Cookie oluşturma
    resp = make_response("Cookie oluşturuldu!")
    resp.set_cookie('kullanici_adi', 'ahmet')
    return resp

@app.route('/cookie_oku')
def cookie_oku():
    # Cookie okuma
    kullanici_adi = request.cookies.get('kullanici_adi')
    return f'Kullanıcı Adı: {kullanici_adi}'

if __name__ == '__main__':
    app.run(debug=True)
    
