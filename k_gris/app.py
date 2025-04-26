from flask import Flask, render_template, request, redirect, url_for, session, flash
import sqlite3

app = Flask(__name__)
app.secret_key = '34f049a15187e6b14f0b36bd'  # Oturum yönetimi için gizli anahtar

# Veritabanı bağlantısı
def get_db_connection():
    conn = sqlite3.connect('users.db')
    conn.row_factory = sqlite3.Row
    return conn

# Ana sayfa
@app.route('/')
def home():
    if 'username' in session:
     return redirect(url_for('index'))
    return redirect(url_for('login'))

# Kullanıcı girişi
@app.route('/login', methods=['GET', 'POST'])#bir nevi ceo url aslında
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn = get_db_connection()
        user = conn.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password)).fetchone()
        conn.close()

        if user:
            session['username'] = user['username']
            return redirect(url_for('index'))
        else:
            flash('Gecersiz kullanici adi veya sifre!')
    return render_template('login.html')

# Kullanıcı kaydı
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn = get_db_connection()
        try:
            conn.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
            conn.commit()
            flash('Kayit basarili! Lutfen giris yapin.')
        except sqlite3.IntegrityError:
            flash('Bu kullanici adi zaten alinmis!')
        finally:
            conn.close()

        return redirect(url_for('login'))
    return render_template('register.html')

# Hoşgeldin sayfası
@app.route('/index')
def index():
    if 'username' in session:
        return render_template('index.html', username=session['username'])  # Kullanıcı adını şablona gönder
    return redirect(url_for('login'))

# Çıkış yap
@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)