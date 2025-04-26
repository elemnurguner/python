from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Güvenlik için gizli bir anahtar

# Basit bir kullanıcı veritabanı (gerçek bir uygulamada bir veritabanı kullanılmalıdır)
users = {}

@app.route('/')
def home():
    if 'username' in session:
        return f'Merhaba, {session["username"]}! <a href="/logout">Çıkış Yap</a>'
    return 'Ana Sayfa <a href="/login">Giriş Yap</a> | <a href="/register">Kayıt Ol</a>'

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users:
            return 'Bu kullanıcı adı zaten alınmış!'
        users[username] = password
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username] == password:
            session['username'] = username
            return redirect(url_for('home'))
        return 'Geçersiz kullanıcı adı veya şifre!'
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)