import csv
#yazılacak veriler

veriler=[
    {'ad':'Ali','soyad':'Yılmaz','yas':25,'sehir':'Ankara'},
    {'ad':'Ayşe','soyad':'Demir','yas':30,'sehir':'İstanbul'},
    
]
#csv dosyasına yazma
with open('veriler.csv',mode='w',encoding='utf-8',newline='')as dosya:
    alan_adlari=['ad','soyad','yas','sehir']
    yazici=csv.DictWriter(dosya,fieldnames=alan_adlari)
    
    yazici.writeheader()#alan adlarını yazdır
    yazici.writerows(veriler)#verileri yazdır