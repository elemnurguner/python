# SQLite veritabanı ile çalışmak için gerekli modülü içe aktar
import sqlite3

# Veritabanı bağlantısı oluştur (banka.db adında bir dosya oluşturur veya varsa ona bağlanır)
conn = sqlite3.connect('banka.db')
# Veritabanı üzerinde işlem yapmak için bir cursor (imleç) oluştur
cursor = conn.cursor()

# Kullanicilar tablosunu oluştur (eğer zaten yoksa)
cursor.execute('''
CREATE TABLE IF NOT EXISTS Kullanicilar (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ad TEXT NOT NULL,
    soyad TEXT NOT NULL,
    tc_kimlik TEXT UNIQUE NOT NULL,
    sifre TEXT NOT NULL
)
''')

# Hesaplar tablosunu oluştur (eğer zaten yoksa)
cursor.execute('''
CREATE TABLE IF NOT EXISTS Hesaplar (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    kullanici_id INTEGER,
    bakiye REAL DEFAULT 0,
    FOREIGN KEY (kullanici_id) REFERENCES Kullanicilar(id)
)
''')

# Veritabanındaki değişiklikleri kaydet
conn.commit()

# Kullanıcı sınıfı
class Kullanici:
    def __init__(self, ad, soyad, tc_kimlik, sifre):
        # Kullanıcı bilgilerini sakla
        self.ad = ad
        self.soyad = soyad
        self.tc_kimlik = tc_kimlik
        self.sifre = sifre

    # Kullanıcı kaydolma metodu
    def kaydol(self):
        # Kullanicilar tablosuna yeni bir kullanıcı ekle
        cursor.execute('''
        INSERT INTO Kullanicilar (ad, soyad, tc_kimlik, sifre)
        VALUES (?, ?, ?, ?)
        ''', (self.ad, self.soyad, self.tc_kimlik, self.sifre))
        # Değişiklikleri veritabanına kaydet
        conn.commit()
        print("Kayıt başarılı!")

    # Kullanıcı giriş yapma metodu (statik metod)
    @staticmethod
    def giris_yap(tc_kimlik, sifre):
        # Kullanıcıyı TC Kimlik ve şifre ile sorgula
        cursor.execute('''
        SELECT id, ad, soyad FROM Kullanicilar
        WHERE tc_kimlik = ? AND sifre = ?
        ''', (tc_kimlik, sifre))
        # Sorgu sonucunu al
        kullanici = cursor.fetchone()
        if kullanici:
            # Kullanıcı bulunduysa hoş geldin mesajı göster ve kullanıcı ID'sini döndür
            print(f"Hoş geldiniz, {kullanici[1]} {kullanici[2]}!")
            return kullanici[0]  # Kullanıcı ID'sini döndür
        else:
            # Kullanıcı bulunamadıysa hata mesajı göster
            print("Geçersiz TC Kimlik veya şifre.")
            return None

# Hesap sınıfı
class Hesap:
    def __init__(self, kullanici_id):
        # Kullanıcı ID'sini sakla ve yeni bir hesap oluştur
        self.kullanici_id = kullanici_id
        self.hesap_id = self.hesap_olustur()

    # Yeni hesap oluşturma metodu
    def hesap_olustur(self):
        # Hesaplar tablosuna yeni bir hesap ekle
        cursor.execute('''
        INSERT INTO Hesaplar (kullanici_id)
        VALUES (?)
        ''', (self.kullanici_id,))
        # Değişiklikleri veritabanına kaydet
        conn.commit()
        # Oluşturulan hesabın ID'sini döndür
        return cursor.lastrowid

    # Para yatırma metodu
    def para_yatir(self, miktar):
        # Hesabın bakiyesini güncelle
        cursor.execute('''
        UPDATE Hesaplar
        SET bakiye = bakiye + ?
        WHERE id = ?
        ''', (miktar, self.hesap_id))
        # Değişiklikleri veritabanına kaydet
        conn.commit()
        print(f"{miktar} TL yatırıldı.")

    # Para çekme metodu
    def para_cek(self, miktar):
        # Hesabın bakiyesini sorgula
        cursor.execute('''
        SELECT bakiye FROM Hesaplar
        WHERE id = ?
        ''', (self.hesap_id,))
        bakiye = cursor.fetchone()[0]
        if bakiye >= miktar:
            # Bakiye yeterliyse para çek
            cursor.execute('''
            UPDATE Hesaplar
            SET bakiye = bakiye - ?
            WHERE id = ?
            ''', (miktar, self.hesap_id))
            conn.commit()
            print(f"{miktar} TL çekildi.")
        else:
            # Bakiye yetersizse hata mesajı göster
            print("Yetersiz bakiye.")

    # Bakiye sorgulama metodu
    def bakiye_sorgula(self):
        # Hesabın bakiyesini sorgula
        cursor.execute('''
        SELECT bakiye FROM Hesaplar
        WHERE id = ?
        ''', (self.hesap_id,))
        bakiye = cursor.fetchone()[0]
        print(f"Güncel bakiye: {bakiye} TL")

# Ana program fonksiyonu
def main():
    while True:
        # Kullanıcıya seçenekleri göster
        print("\n1. Kaydol\n2. Giriş Yap\n3. Çıkış")
        secim = input("Seçiminiz: ")

        if secim == "1":
            # Kullanıcıdan bilgileri al ve kaydol
            ad = input("Ad: ")
            soyad = input("Soyad: ")
            tc_kimlik = input("TC Kimlik: ")
            sifre = input("Şifre: ")
            kullanici = Kullanici(ad, soyad, tc_kimlik, sifre)
            kullanici.kaydol()

        elif secim == "2":
            # Kullanıcıdan TC Kimlik ve şifre al ve giriş yap
            tc_kimlik = input("TC Kimlik: ")
            sifre = input("Şifre: ")
            kullanici_id = Kullanici.giris_yap(tc_kimlik, sifre)
            if kullanici_id:
                # Giriş başarılıysa hesap işlemlerini yönet
                hesap = Hesap(kullanici_id)
                while True:
                    print("\n1. Para Yatır\n2. Para Çek\n3. Bakiye Sorgula\n4. Çıkış")
                    hesap_secim = input("Seçiminiz: ")
                    if hesap_secim == "1":
                        miktar = float(input("Yatırılacak miktar: "))
                        hesap.para_yatir(miktar)
                    elif hesap_secim == "2":
                        miktar = float(input("Çekilecek miktar: "))
                        hesap.para_cek(miktar)
                    elif hesap_secim == "3":
                        hesap.bakiye_sorgula()
                    elif hesap_secim == "4":
                        break
                    else:
                        print("Geçersiz seçim.")

        elif secim == "3":
            # Programdan çık
            print("Çıkış yapılıyor...")
            break

        else:
            # Geçersiz seçim durumunda uyarı göster
            print("Geçersiz seçim.")

# Program çalıştırıldığında main fonksiyonunu çağır
if __name__ == "__main__":
    main()

# Veritabanı bağlantısını kapat
conn.close()