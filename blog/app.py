import sqlite3
from flask import Flask, render_template, request, redirect, url_for

# Flask uygulamasını oluştur
app = Flask(__name__)

# SQLite veritabanı dosyasının adı
DATABASE = 'blog.db'

# Veritabanı bağlantısını oluşturan fonksiyon
def get_db_connection():
    conn = sqlite3.connect(DATABASE)  # Veritabanına bağlan
    conn.row_factory = sqlite3.Row  # Sorgu sonuçlarını sözlük benzeri bir yapıda al
    return conn

# Veritabanını başlatan fonksiyon (tabloyu oluşturur)
def init_db():
    conn = get_db_connection()
    conn.execute('CREATE TABLE IF NOT EXISTS posts (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT NOT NULL, content TEXT NOT NULL)')
    conn.commit()  # Değişiklikleri kaydet
    conn.close()  # Bağlantıyı kapat

# Ana sayfa route'u
@app.route('/')
def index():
    conn = get_db_connection()  # Veritabanına bağlan
    posts = conn.execute('SELECT * FROM posts').fetchall()  # Tüm gönderileri al
    conn.close()  # Bağlantıyı kapat
    return render_template('index.html', posts=posts)  # index.html şablonunu göster

# Gönderi ekleme route'u
@app.route('/add', methods=['GET', 'POST'])
def add_post():
    if request.method == 'POST':  # Form gönderildiyse
        title = request.form['title']  # Formdan başlık al
        content = request.form['content']  # Formdan içerik al
        conn = get_db_connection()  # Veritabanına bağlan
        conn.execute('INSERT INTO posts (title, content) VALUES (?, ?)', (title, content))  # Yeni gönderi ekle
        conn.commit()  # Değişiklikleri kaydet
        conn.close()  # Bağlantıyı kapat
        return redirect(url_for('index'))  # Ana sayfaya yönlendir
    return render_template('add_post.html')  # add_post.html şablonunu göster

# Gönderi düzenleme route'u
@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_post(id):
    conn = get_db_connection()  # Veritabanına bağlan
    post = conn.execute('SELECT * FROM posts WHERE id = ?', (id,)).fetchone()  # Düzenlenecek gönderiyi al
    if request.method == 'POST':  # Form gönderildiyse
        title = request.form['title']  # Formdan başlık al
        content = request.form['content']  # Formdan içerik al
        conn.execute('UPDATE posts SET title = ?, content = ? WHERE id = ?', (title, content, id))  # Gönderiyi güncelle
        conn.commit()  # Değişiklikleri kaydet
        conn.close()  # Bağlantıyı kapat
        return redirect(url_for('index'))  # Ana sayfaya yönlendir
    conn.close()  # Bağlantıyı kapat
    return render_template('edit_post.html', post=post)  # edit_post.html şablonunu göster

# Gönderi silme route'u
@app.route('/delete/<int:id>')
def delete_post(id):
    conn = get_db_connection()  # Veritabanına bağlan
    conn.execute('DELETE FROM posts WHERE id = ?', (id,))  # Gönderiyi sil
    conn.commit()  # Değişiklikleri kaydet
    conn.close()  # Bağlantıyı kapat
    return redirect(url_for('index'))  # Ana sayfaya yönlendir

# Uygulamayı çalıştır
if __name__ == '__main__':
    init_db()  # Veritabanını başlat
    app.run(debug=True)  # Uygulamayı debug modunda çalıştır