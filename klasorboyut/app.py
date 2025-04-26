import os

def klasor_boyutu_hesapla(klasor_yolu):
    toplam_boyut = 0

    # Klasör içindeki tüm dosya ve alt klasörleri gez
    for klasor_ici_yol, _, dosyalar in os.walk(klasor_yolu):
        for dosya in dosyalar:
            dosya_yolu = os.path.join(klasor_ici_yol, dosya)
            toplam_boyut += os.path.getsize(dosya_yolu)

    return toplam_boyut

# Klasör yolunu belirtin burda yater çizgi olmalı / olmalı yada  çift düz çizgi\\
klasor_yolu = "C:\\Users\\USER\\Desktop\\acil_projeler_ysa_data\\python\\klasorboyut\\test"  # Buraya hesaplamak istediğiniz klasörün yolunu yazın

# Klasör boyutunu hesapla
boyut = klasor_boyutu_hesapla(klasor_yolu)

# Sonucu okuyabilir bir formatta göster
print(f"Klasör Boyutu: {boyut} byte")
print(f"Klasör Boyutu: {boyut / 1024:.2f} KB")
print(f"Klasör Boyutu: {boyut / (1024 * 1024):.2f} MB")
print(f"Klasör Boyutu: {boyut / (1024 * 1024 * 1024):.2f} GB")