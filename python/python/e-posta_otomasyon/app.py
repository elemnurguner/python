from flask import Flask, render_template, request, redirect, url_for, flash
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)
app.secret_key = '3e4f5a6b7c8d9e0f1a2b3c4d5e6f7a8b'  # Flash mesajları için gerekli

# Gmail SMTP ayarları
GÖNDERICI_EMAIL = "elemnurguner@gmail.com"  # Gmail adresiniz
ŞIFRE = "szsz gzru bsun hcts"  # Uygulama şifreniz email den alıyoruz bunu 
SMTP_SUNUCU = "smtp.gmail.com"
SMTP_PORT = 587

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        alıcı_email = request.form['alıcı_email']
        konu = request.form['konu']
        mesaj = request.form['mesaj']

        # E-posta içeriğini HTML şablonu ile oluştur gonderilen template aslında biz oluşturduk otomatik falan gonderilmiştirkısmını 
        email_icerik = render_template('email_template.html', mesaj=mesaj)

        # E-posta oluşturma
        msg = MIMEMultipart()
        msg['From'] = GÖNDERICI_EMAIL
        msg['To'] = alıcı_email
        msg['Subject'] = konu
        msg.attach(MIMEText(email_icerik, 'html'))  # HTML içeriği ekle

        try:
            # SMTP sunucusuna bağlanma ve e-posta gönderme
            server = smtplib.SMTP(SMTP_SUNUCU, SMTP_PORT)
            server.starttls()  # Güvenli bağlantı
            server.login(GÖNDERICI_EMAIL, ŞIFRE)
            server.sendmail(GÖNDERICI_EMAIL, alıcı_email, msg.as_string())
            server.quit()
            flash('E-posta başarıyla gönderildi!', 'success')
        except Exception as e:
            flash(f'E-posta gönderilirken hata oluştu: {e}', 'error')

        return redirect(url_for('index'))

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)