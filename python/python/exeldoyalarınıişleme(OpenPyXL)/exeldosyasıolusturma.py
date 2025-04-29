from openpyxl import Workbook

# Yeni bir Excel dosyası oluştur	
workbook=Workbook()
sheet=workbook.active

#başlık satırını ekle
sheet.append(["Ad", "Soyad", "Yaş","Not"])

#Örnek verileri ekle
sheet.append(["Ali", "Yılmaz", 25, 85]) 
sheet.append(["Ayşe", "Demir", 22, 90])
sheet.append(["Mehmet", "Kara", 23, 75])
sheet.append(["Fatma", "Kaya", 24, 80])
sheet.append(["Hüseyin", "Yıldız", 26, 95])
sheet.append(["Zeynep", "Kurt", 21, 70])

#dosyayı kaydet
dosya_adi="ogrenciler.xlsx"
workbook.save(dosya_adi)
print(f"{dosya_adi} adlı dosya oluşturuldu.")