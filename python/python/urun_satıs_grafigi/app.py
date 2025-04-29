from flask import Flask, render_template, jsonify

app = Flask(__name__)

# Örnek satış verileri
satis_verileri = {
    "aylar": ["Ocak", "Şubat", "Mart", "Nisan", "Mayıs", "Haziran"],
    "satislar": [65, 59, 80, 81, 56, 55]
}

@app.route("/")
def anasayfa():
    return render_template("index.html")

@app.route("/veriler")
def veriler():
    return jsonify(satis_verileri)

if __name__ == "__main__":
    app.run(debug=True)