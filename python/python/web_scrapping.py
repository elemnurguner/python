import requests
from bs4 import BeautifulSoup
import csv

# Web sayfasının URL'si
url = "http://books.toscrape.com/"

# Web sayfasının içeriğini çekme
response = requests.get(url)

# Sayfanın kodlamasını otomatik olarak belirleme
response.encoding = response.apparent_encoding

# HTTP isteğinin başarılı olup olmadığını kontrol etme
if response.status_code == 200:
    # HTML içeriğini parse etme
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Tüm kitap bilgilerini içeren etiketleri bulma
    books = soup.find_all('article', class_='product_pod')
    
    # Çekilen verileri bir CSV dosyasına kaydetme
    with open('books.csv', 'w', newline='', encoding='utf-8-sig') as file:
        writer = csv.writer(file)
        # CSV başlıkları
        writer.writerow(['Kitap Adı', 'Fiyat'])
        
        # Her bir kitap için bilgileri çekme
        for book in books:
            title = book.h3.a['title']  # Kitap adı
            price = book.find('p', class_='price_color').text  # Kitap fiyatı
            
            # Fiyattaki gereksiz karakterleri temizleme
            price = price.replace('Â', '')  # Â karakterini kaldır
            
            writer.writerow([title, price])
    
    print("Veriler başarıyla 'books.csv' dosyasına kaydedildi.")
else:
    print(f"Sayfa çekilemedi. HTTP Hata Kodu: {response.status_code}")
    
#Fiyatları Temizleme:
# Fiyatları çekerken, Â£ gibi gereksiz karakterleri kaldırmak için bir temizleme işlemi uygulayabiliriz.