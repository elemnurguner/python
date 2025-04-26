from datetime import datetime

# Kullanıcıdan tarih al (örnek format: GG/AA/YYYY)
tarih_str = input("Tarihi GG/AA/YYYY formatında girin: ")

# String'i datetime nesnesine çevir
tarih = datetime.strptime(tarih_str, "%d/%m/%Y")

# Farklı formatlarda tarihi göster
print("Orijinal Tarih:", tarih_str)
print("ISO Formatı:", tarih.isoformat())
print("YYYY-AA-GG Formatı:", tarih.strftime("%Y-%m-%d"))
print("GG.AA.YYYY Formatı:", tarih.strftime("%d.%m.%Y"))
print("AA/GG/YYYY Formatı:", tarih.strftime("%m/%d/%Y"))
print("Gün/Ay/Yıl:", tarih.strftime("%d %B %Y"))
print("Kısa Tarih:", tarih.strftime("%d %b %Y"))