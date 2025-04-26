from openpyxl import Workbook

#yeni bir exel dosyası oluştur
workbook=Workbook()

#ilk çalışma sayfasuna  veri ekle
sheet=workbook.active
sheet.title="Öğrenciler"
sheet.append(["Ad","Soyad","Yaş","Not"])
sheet.append(["Ali","Yılmaz",22,90])
sheet.append(["Ayşe","Demir",23,85])
#ikinci çalışma sayfası oluştur
sheet2=workbook.create_sheet("Dersler")
sheet2.append(["Ders Kodu","Ders Adı","Kredi"])
sheet2.append(["MAT101","Matematik",6])
sheet2.append(["FZK101","Fizik",5])

#Dosyayı kaydet
workbook.save("birdenfazlakayit.xlsx")
