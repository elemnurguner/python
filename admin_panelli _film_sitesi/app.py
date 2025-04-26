import os
import json
from flask import Flask, render_template, request, redirect, url_for, flash
from werkzeug.utils import secure_filename
from PIL import Image
from forms import FilmEkleForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "super_secret_key"
app.config["UPLOAD_FOLDER"] = "static/uploads"
app.config["IMAGE_SIZE"] = (300, 450)  # Resim boyutu (genişlik, yükseklik)

# Eğer upload klasörü yoksa oluştur
if not os.path.exists(app.config["UPLOAD_FOLDER"]):
    os.makedirs(app.config["UPLOAD_FOLDER"])

# Filmleri saklamak için JSON dosyası
FILMLER_JSON = "films.json"

# Film listesini yükleyen fonksiyon
def load_films():
    if os.path.exists(FILMLER_JSON):
        with open(FILMLER_JSON, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

# Filmleri kaydeden fonksiyon
def save_films(films):
    with open(FILMLER_JSON, "w", encoding="utf-8") as f:
        json.dump(films, f, ensure_ascii=False, indent=4)

@app.route("/", methods=["GET"])
def index():
    filmler = load_films()
    return render_template("index.html", filmler=filmler)

@app.route("/film-ekle", methods=["GET", "POST"])
def film_ekle():
    form = FilmEkleForm()
    if form.validate_on_submit():
        # Dosya işlemleri
        file = form.resim.data
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config["UPLOAD_FOLDER"], filename)

        # Resmi belirli bir boyuta getir
        image = Image.open(file)
        image = image.resize(app.config["IMAGE_SIZE"])
        image.save(filepath)

        # JSON'a yeni filmi ekle
        filmler = load_films()
        yeni_film = {"ad": form.ad.data, "resim": filename}
        filmler.append(yeni_film)
        save_films(filmler)

        flash("Film başarıyla eklendi!", "success")
        return redirect(url_for("index"))

    return render_template("film_ekle.html", form=form)

if __name__ == "__main__":
    app.run(debug=True)
