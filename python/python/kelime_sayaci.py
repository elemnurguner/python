def kelime_sayaci(dosya_adi):
    try:
        #dosyayıaç ve içini oku
        with open(dosya_adi, "r") as dosya:
            metin = dosya.read()
        #kelimeleri boşluklara  göre ayır ve sayısını hesapla
        kelimeler = metin.split()
        kelime_sayisi = len(kelimeler)
    
        print(f"{dosya_adi} dosyasında toplam {kelime_sayisi} kelime bulunmaktadır.")
    except FileNotFoundError:
        print(f"Hata: '{dosya_adi}' dosyası bulunamadı.")
    except Exception as e:
        print(f"Hata oluştu: {e}")

# Kullanıcıdan dosya adını alalım
dosya_adi = input("Kelime sayısını hesaplamak istediğiniz dosyanın adını girin: ")
kelime_sayaci(dosya_adi)
    