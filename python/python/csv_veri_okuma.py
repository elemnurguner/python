import csv

# CSV dosyasını okuma
with open('veriler.csv', mode='r', encoding='utf-8') as dosya:
    okuyucu = csv.DictReader(dosya)  # Satırları sözlük olarak okur
    for satir in okuyucu:
        print(satir)  # Her satırı yazdır