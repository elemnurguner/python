from flask import Flask, render_template, request, redirect, url_for, g, send_from_directory
import sqlite3
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'  # Resimlerin kaydedileceği klasör
DATABASE = 'personel.db'

# Resim klasörü yoksa oluştur
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

# Veritabanı bağlantısı
def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
        db.row_factory = sqlite3.Row  # Sütun isimleriyle erişim sağlar
    return db

# Uygulama sonlandığında veritabanı bağlantısını kapat
@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

# Tablo oluşturma (İlk çalıştırmada gerekli)
def init_db():
    with app.app_context():#???
        db = get_db()
        cursor = db.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS personel (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                ad TEXT NOT NULL,
                soyad TEXT NOT NULL,
                departman TEXT NOT NULL,
                maas REAL NOT NULL,
                resim TEXT
            )
        ''')
        db.commit()
        
        
# Resim dosyalarını sunma
@app.route('/uploads/<filename>')#????
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)#????????????#sen  form drectory g gibiglobal bir değişken istemsiye gondermek için 


# Departman listesi
DEPARTMANLAR = ["IT", "İnsan Kaynakları", "Muhasebe", "Satış"]
#anasayfadan gelen işlemler 
@app.route('/')
def index():
    departman = request.args.get('departman')  # Departman filtresi
    db = get_db()
    cursor = db.cursor()#cursor benim sorgu yapmama işe yarıyor du 
    
    if departman and departman != "Tüm Departmanlar":  # Filtre uygula
        cursor.execute('SELECT * FROM personel WHERE departman = ?', (departman,))#neden virül koydun sonrasına  ???
    else:  # Tüm personelleri getir
        cursor.execute('SELECT * FROM personel')

    personeller = cursor.fetchall()
    return render_template('index.html', personeller=personeller, departmanlar=DEPARTMANLAR)#seçiliyse işlem yapar değilde direkt getirir zaten

@app.route('/ekle', methods=['GET', 'POST'])
def ekle():
    if request.method == 'POST':
        ad = request.form['ad']
        soyad = request.form['soyad']
        departman = request.form['departman']
        maas = request.form['maas']
        resim = request.files['resim']

        # Resmi kaydet
        if resim:
            resim_yolu = os.path.join(app.config['UPLOAD_FOLDER'], resim.filename)#??
            resim.save(resim_yolu)
        else:
            resim_yolu = None
            
        db = get_db()
        cursor = db.cursor()
        cursor.execute('''
            INSERT INTO personel (ad, soyad, departman, maas, resim)
            VALUES (?, ?, ?, ?, ?)
        ''', (ad, soyad, departman, maas, resim.filename if resim else None))
        db.commit()
        return redirect(url_for('index'))
    return render_template('ekle.html', departmanlar=DEPARTMANLAR)

# Personel Güncelleme
@app.route('/guncelle/<int:id>', methods=['GET', 'POST'])
def guncelle(id):
    db = get_db()
    cursor = db.cursor()

    if request.method == 'POST':
        ad = request.form['ad']
        soyad = request.form['soyad']
        departman = request.form['departman']
        maas = request.form['maas']
        resim = request.files['resim']

        # Resmi güncelle
        if resim:
            resim_yolu = os.path.join(app.config['UPLOAD_FOLDER'], resim.filename)
            resim.save(resim_yolu)
            cursor.execute('''
                UPDATE personel
                SET ad = ?, soyad = ?, departman = ?, maas = ?, resim = ?
                WHERE id = ?
            ''', (ad, soyad, departman, maas, resim.filename, id))
        else:#burda yapılan  işlem  resimin yolu ayrı boyutlandırıp güncellem işlemi yapılacığı için  diğer işlerimi else duruma alıp tekrar guncelledik
            cursor.execute('''
                UPDATE personel
                SET ad = ?, soyad = ?, departman = ?, maas = ?
                WHERE id = ?
            ''', (ad, soyad, departman, maas, id))

        db.commit()
        return redirect(url_for('index'))

    cursor.execute('SELECT * FROM personel WHERE id = ?', (id,))#virgülü  nedn koydum  acaba?
    personel = cursor.fetchone()#gormek için çekmem gerekiyor 
    return render_template('guncelle.html', personel=personel)

# Personel Silme
@app.route('/sil/<int:id>')
def sil(id):
    db = get_db()
    cursor = db.cursor()
    cursor.execute('DELETE FROM personel WHERE id = ?', (id,))
    db.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
   
    app.run(debug=True)