# Flask kütüphanesini ve gerekli modülleri içe aktar
from flask import Flask, render_template, request, redirect, url_for, send_from_directory, session
# Resim işlemleri için Pillow kütüphanesini içe aktar
from PIL import Image
# Dosya işlemleri için os modülünü içe aktar
import os

# Flask uygulamasını oluştur
app = Flask(__name__)
# Session (oturum) için gizli anahtar belirle
# Bu anahtar, session verilerini şifrelemek için kullanılır
app.secret_key = '3f4a5b6c7d8e9f0a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8g9h0i1j2k3l4m5n6o7p8'  # Session için gizli anahtar

# Kullanıcı veritabanı (geçici olarak liste kullanıyoruz)# Basit bir kullanıcı veritabanı oluştur (kullanıcı adı ve şifre)
kullanicilar = {
    'admin': '1234',
    'user': 'password'
}

# Dosya yükleme ayarlarını belirle
# Yüklenen dosyaların kaydedileceği klasörü tanımla
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'gif'}

# Her kullanıcının stok bilgilerini saklamak için bir sözlük oluştur
stoklar = {}

# İzin verilen dosya uzantılarını kontrol eden fonksiyon
def allowed_file(filename):
     # Dosya adında nokta (.) var mı ve uzantısı izin verilenler arasında mı kontrol et
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

# Resmi küçültme fonksiyonu
def resize_image(image_path, output_path, size=(200, 200)):
    # Resmi aç
    with Image.open(image_path) as img:
        # Resmi belirtilen boyuta küçült
        img.thumbnail(size)
        # Küçültülmüş resmi kaydet
        img.save(output_path)


# Ana sayfa route'u
@app.route('/')
def index():
    if 'kullanici' not in session:
        return redirect(url_for('giris'))
    kullanici_stoklari = stoklar.get(session['kullanici'], [])
    kullanici_stoklari = sorted(kullanici_stoklari, key=lambda x: x['urun_adi'])  # İsme göre sırala
    # index.html şablonunu render et ve stokları şablona gönder
    return render_template('index.html', stoklar=kullanici_stoklari)

# Giriş sayfası
@app.route('/giris', methods=['GET', 'POST'])
def giris():
# POST isteği geldiyse (form gönderildiyse)    
    if request.method == 'POST':
        kullanici_adi = request.form['kullanici_adi']
        sifre = request.form['sifre']
        #kullanıcı adındaki kullanıcılar ve kullanıcıların  içindeki kullanıcı adı ile  şifre dogru ise
        if kullanici_adi in kullanicilar and kullanicilar[kullanici_adi] == sifre:
            # Session'a kullanıcı adını kaydet
            session['kullanici'] = kullanici_adi
            # Ana sayfaya yönlendir
            return redirect(url_for('index'))
        else:
            return "Hatalı kullanıcı adı veya şifre!"
    return render_template('giris.html')

# Çıkış yap
@app.route('/cikis')
def cikis():
 # Session'dan kullanıcı bilgisini sil
    session.pop('kullanici', None)
    return redirect(url_for('giris'))

# Stok ekleme route'u
@app.route('/stok_ekle', methods=['POST'])
def stok_ekle():
    if 'kullanici' not in session:
        return redirect(url_for('giris'))

    kullanici = session['kullanici']
    urun_adi = request.form['urun_adi']
    stok_miktari = request.form['stok_miktari']
    dosya = request.files['urun_foto']

    # Aynı isimde ürün kontrolü
    if kullanici in stoklar:
        for stok in stoklar[kullanici]:
            if stok['urun_adi'] == urun_adi:
                return "Bu isimde bir ürün zaten var!"#stok stoklar kısmı birer statik değişkendir verileri almak için kullandık  tek tek kullanıcı urun bilgisini dondurmem gerek bunun için  for kullandım 

 # Dosya yüklendiyse ve uzantısı izin verilenler arasındaysa
    if dosya and allowed_file(dosya.filename):
        # Dosya adını ve yolunu belirle
        filename = dosya.filename
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)#?????
         # Dosyayı kaydet
        dosya.save(filepath)

         # Resmi küçült ve yeni dosya adını belirle
        resized_filename = f"resized_{filename}"
        resized_filepath = os.path.join(app.config['UPLOAD_FOLDER'], resized_filename)
        resize_image(filepath, resized_filepath)

        # Kullanıcının stok listesi yoksa oluştur
        if kullanici not in stoklar:
            stoklar[kullanici] = []
        # Yeni stok bilgilerini listeye ekle
        stoklar[kullanici].append({
            'id': len(stoklar[kullanici]) + 1, # Otomatik ID oluştur#????
            'urun_adi': urun_adi,
            'stok_miktari': stok_miktari,
            'foto': resized_filename
        })

    return redirect(url_for('index'))#anasayfaya yonlendir

# Stok Silme
@app.route('/stok_sil/<int:id>')
def stok_sil(id):
    if 'kullanici' not in session:
        return redirect(url_for('giris'))
    # Session'dan kullanıcı adını al
    kullanici = session['kullanici']
    if kullanici in stoklar:    # Kullanıcının stok listesi varsa
 # Silinecek stok öğesini bul
        stok = next((s for s in stoklar[kullanici] if s['id'] == id), None)#??????
        if stok:
 # Stok öğesine ait resmi sil
            foto_path = os.path.join(app.config['UPLOAD_FOLDER'], stok['foto'])
            if os.path.exists(foto_path):
                os.remove(foto_path)
# Stok öğesini listeden kaldır
            stoklar[kullanici] = [s for s in stoklar[kullanici] if s['id'] != id]#???????????
    return redirect(url_for('index'))


# Stok güncelleme route'u
@app.route('/stok_guncelle/<int:id>', methods=['GET', 'POST'])
def stok_guncelle(id):
    if 'kullanici' not in session:
        return redirect(url_for('giris'))
# Session'dan kullanıcı adını al
    kullanici = session['kullanici']
    if kullanici not in stoklar:    # Kullanıcının stok listesi yoksa ana sayfaya yönlendir
        return redirect(url_for('index'))
# Güncellenecek stok öğesini bul
    stok = next((s for s in stoklar[kullanici] if s['id'] == id), None)#??????????
    if not stok:
        return redirect(url_for('index'))
 # POST isteği geldiyse (form gönderildiyse)
    if request.method == 'POST':
        stok['urun_adi'] = request.form['urun_adi']
        stok['stok_miktari'] = request.form['stok_miktari']
        dosya = request.files['urun_foto']
        
# Yeni dosya yüklendiyse ve uzantısı izin verilenler arasındaysa
        if dosya and allowed_file(dosya.filename):
            # Eski resmi sil
            eski_foto_path = os.path.join(app.config['UPLOAD_FOLDER'], stok['foto'])
            if os.path.exists(eski_foto_path):
                os.remove(eski_foto_path)

            # Yeni resmi kaydet ve küçült
            filename = dosya.filename
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            dosya.save(filepath)

            resized_filename = f"resized_{filename}"
            resized_filepath = os.path.join(app.config['UPLOAD_FOLDER'], resized_filename)
            resize_image(filepath, resized_filepath)
# Stok öğesinin resim bilgisini güncelle
            stok['foto'] = resized_filename

        return redirect(url_for('index'))
# GET isteği geldiyse stok_guncelle.html şablonunu render et ve stok bilgisini gönder
    return render_template('stok_guncelle.html', stok=stok)

# Yüklenen resimlere erişim
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    # Yüklenen resmi kullanıcıya gönder
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    # Uploads klasörü yoksa oluştur
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])
    app.run(debug=True) # Uygulamayı debug modunda çalıştır
