#qr kod  uretici yapmak  için bir  programlama dili  kullanabilirz qrcode kutuphanesini indiricez bash e pip install qrcode[pil]
import qrcode

def generate_qr_code(data, file_name='qrcode.png'):
    # QR kod nesnesi oluştur
    qr = qrcode.QRCode(
        version=1,  # QR kod versiyonu (1-40 arası)
        error_correction=qrcode.constants.ERROR_CORRECT_L,  # Hata düzeltme seviyesi
        box_size=10,  # Her bir kutunun boyutu
        border=4,  # Kenar boşluğu
    )
    
    # QR koda eklenecek veriyi ekle
    qr.add_data(data)
    qr.make(fit=True)
    
    # QR kodunu resim olarak oluştur
    img = qr.make_image(fill_color="black", back_color="white")
    
    # Resmi dosya olarak kaydet
    img.save(file_name)
    print(f"QR kodu '{file_name}' olarak kaydedildi.")

# Kullanım örneği
data = "https://www.example.com"
generate_qr_code(data, 'example_qr.png')