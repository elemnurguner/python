import sqlite3

def db_baglan():
    return sqlite3.connect("veritabani.db")

def tablo_olustur():
    con = db_baglan()
    cur = con.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS filmler (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            isim TEXT NOT NULL,
            aciklama TEXT,
            yayin_tarihi TEXT,
            afis TEXT
        )
    """)
    con.commit()
    con.close()

def film_ekle(isim, aciklama, yayin_tarihi, afis):
    con = db_baglan()
    cur = con.cursor()
    cur.execute("INSERT INTO filmler (isim, aciklama, yayin_tarihi, afis) VALUES (?, ?, ?, ?)", 
                (isim, aciklama, yayin_tarihi, afis))
    con.commit()
    con.close()

def filmleri_getir():
    con = db_baglan()
    cur = con.cursor()
    cur.execute("SELECT * FROM filmler")
    filmler = cur.fetchall()
    con.close()
    return filmler
