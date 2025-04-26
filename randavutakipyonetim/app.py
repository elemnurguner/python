from flask import Flask, render_template, request, redirect, url_for
from models import Randevu
app = Flask(__name__)

# Randevu listesi (geçici veri deposu)
randevular = []

@app.route('/')
def index():
    return render_template('index.html', randevular=randevular)

@app.route('/randevu_ekle', methods=['GET', 'POST'])
def randevu_ekle():
    if request.method == 'POST':
        yeni_randevu =Randevu(
            id=len(randevular) + 1,
            kullanici_adi=request.form['kullanici_adi'],
            tarih=request.form['tarih'],
            saat=request.form['saat'],
            aciklama=request.form['aciklama']
        )
        randevular.append(yeni_randevu)
        return redirect(url_for('index'))
    return render_template('randevu_ekle.html')

@app.route('/randevu_sil/<int:id>')
def randevu_sil(id):
    global randevular
    randevular = [r for r in randevular if r.id != id]
    return redirect(url_for('index'))

@app.route('/randevu_guncelle/<int:id>', methods=['GET', 'POST'])
def randevu_guncelle(id):
    randevu = next((r for r in randevular if r.id == id), None)
    if request.method == 'POST':
        randevu.kullanici_adi = request.form['kullanici_adi']
        randevu.tarih = request.form['tarih']
        randevu.saat = request.form['saat']
        randevu.aciklama = request.form['aciklama']
        return redirect(url_for('index'))
    return render_template('randevu_guncelle.html', randevu=randevu)

if __name__ == '__main__':
    app.run(debug=True)