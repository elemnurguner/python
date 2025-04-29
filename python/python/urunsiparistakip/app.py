from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Flash mesajları için gerekli

# Ürün sınıfı#dınıfın  özellikleini tanımladık bize  ne  gerek 
class Urun:
    def __init__(self, id, ad, fiyat, stok):
        self.id = id
        self.ad = ad
        self.fiyat = fiyat
        self.stok = stok

# Sipariş sınıfı
class Siparis:
    def __init__(self, id, urun_id, miktar, durum="Hazırlanıyor"):
        self.id = id
        self.urun_id = urun_id
        self.miktar = miktar
        self.durum = durum

# Örnek veriler
urunler = [
    Urun(1, "Laptop", 5000, 10),
    Urun(2, "Telefon", 3000, 20),
    Urun(3, "Tablet", 2000, 15)
]

siparisler = []

# CRUD işlemleri
@app.route('/')
def index():
    return render_template('index.html', urunler=urunler, siparisler=siparisler)#urunler temp render edip sipariş ve  urunleri gondericek 

@app.route('/urun_ekle', methods=['POST'])
def urun_ekle():
    ad = request.form['ad']
    fiyat = float(request.form['fiyat'])
    stok = int(request.form['stok'])

    # Aynı ürün adı kontrolü
    for urun in urunler:
        if urun.ad.lower() == ad.lower():
            flash("Bu ürün zaten mevcut!", "danger")
            return redirect(url_for('index'))

    yeni_urun = Urun(len(urunler) + 1, ad, fiyat, stok) # +1 kullanmamın sebebi yeni urunun id sini mevcut urunun sayısının  bir fazlası olarak belirlemktedir aslında sqldeki identitty 1,1 gibi
    urunler.append(yeni_urun)
    flash("Ürün başarıyla eklendi!", "success")
    return redirect(url_for('index'))

@app.route('/siparis_ekle', methods=['POST'])
def siparis_ekle():
    urun_id = int(request.form['urun_id'])
    miktar = int(request.form['miktar'])

    # Ürün stok kontrolü
    urun = next((u for u in urunler if u.id == urun_id), None)
    if not urun:
        flash("Ürün bulunamadı!", "danger")
        return redirect(url_for('index'))

    if urun.stok < miktar:
        flash("Yeterli stok yok!", "danger")
        return redirect(url_for('index'))

    yeni_siparis = Siparis(len(siparisler) + 1, urun_id, miktar)#yeni siparişi  mevcut siparişin  bir fazlası olarak belirleyecek 
    siparisler.append(yeni_siparis)
    flash("Sipariş başarıyla eklendi!", "success")
    return redirect(url_for('index'))

@app.route('/siparis_gonder/<int:siparis_id>')
def siparis_gonder(siparis_id):
    siparis = next((s for s in siparisler if s.id == siparis_id), None)
    if not siparis:
        flash("Sipariş bulunamadı!", "danger")
        return redirect(url_for('index'))

    urun = next((u for u in urunler if u.id == siparis.urun_id), None)#urunlerin içindeki id yi getiriyorum u.id ==siparis.urun_id karşılıklı denkmi 
    if not urun:
        flash("Ürün bulunamadı!", "danger")
        return redirect(url_for('index'))

    if urun.stok < siparis.miktar:
        flash("Yeterli stok yok!", "danger")
        return redirect(url_for('index'))

    # Stoktan düşme ve sipariş durumunu güncelleme
    urun.stok -= siparis.miktar
    siparis.durum = "Gönderildi"
    flash("Sipariş gönderildi ve stok güncellendi!", "success")
    return redirect(url_for('index'))

@app.route('/siparis_sil/<int:siparis_id>')
def siparis_sil(siparis_id):
    global siparisler#siparişler fonksiyon dışında  tanımlanmış bir liste  oldugu için fonk.içinde bu lidteyi değiştir.is.global kullanmamız gerekli 
    siparisler = [s for s in siparisler if s.id != siparis_id]
    flash("Sipariş başarıyla silindi!", "success")
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)