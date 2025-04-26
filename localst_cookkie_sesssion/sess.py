from flask import Flask, session, redirect, url_for, request

app = Flask(__name__)
app.secret_key = '5ddcb0d8cfb0be992b37a674e6dc2c54'

@app.route('/')
def index():
    if 'kullanici_adi' in session:
        return f'Hoş geldiniz, {session["kullanici_adi"]}!'
    return 'Lütfen giriş yapın.'

@app.route('/giris', methods=['GET', 'POST'])
def giris():
    if request.method == 'POST':
        session['kullanici_adi'] = request.form['kullanici_adi']
        return redirect(url_for('index'))
    return '''
        <form method="post">
            Kullanıcı Adı: <input type="text" name="kullanici_adi">
            <input type="submit" value="Giriş Yap">
        </form>
    '''

@app.route('/cikis')
def cikis():
    session.pop('kullanici_adi', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)