from flask import Flask, render_template

app = Flask(__name__)

# Ana sayfa
@app.route('/')
def home():
    return "Ana Sayfa"

# Ürün listesi sayfası
@app.route('/urunler')
def urunler():
    return "Ürün Listesi"

# Tek bir ürün sayfası (CEO URL örneği)
@app.route('/urun/<string:urun_adi>')
def urun_detay(urun_adi):
    return f"{urun_adi} detay sayfası"

# Kategori sayfası (CEO URL örneği)
@app.route('/kategori/<string:kategori_adi>')
def kategori_detay(kategori_adi):
    return f"{kategori_adi} kategorisi"

if __name__ == '__main__':
    app.run(debug=True)