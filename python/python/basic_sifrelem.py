def sifrele(metin, kaydirma):
    sifrelenmis_metin = ""
    for karakter in metin:
        if karakter.isalpha():  # Sadece harfleri şifrele
            # Büyük harf ve küçük harf durumunu koru
            baslangic = ord('A') if karakter.isupper() else ord('a')
            sifrelenmis_metin += chr((ord(karakter) - baslangic + kaydirma) % 26 + baslangic)
        else:
            sifrelenmis_metin += karakter  # Harf değilse olduğu gibi ekle (boşluk, noktalama işaretleri vb.)
    return sifrelenmis_metin

def coz(sifrelenmis_metin, kaydirma):
    return sifrele(sifrelenmis_metin, -kaydirma)  # Şifre çözme, kaydırmayı tersine çevirerek yapılır

# Kullanıcıdan metin ve kaydırma değerini alalım
metin = input("Şifrelemek istediğiniz metni girin: ")
kaydirma = int(input("Kaydırma değerini girin (örn. 3): "))

# Metni şifrele
sifrelenmis_metin = sifrele(metin, kaydirma)
print(f"Şifrelenmiş metin: {sifrelenmis_metin}")

# Şifrelenmiş metni çöz
cozulmus_metin = coz(sifrelenmis_metin, kaydirma)
print(f"Çözülmüş metin: {cozulmus_metin}")