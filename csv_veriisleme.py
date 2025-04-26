import csv
#csv dosyasını okuma ve  yaşı  25 den buyuk olanları listeleme 
# with open('veriler.csv',mode='r',encoding='utf-8') as dosya:
#     okuyucu=csv.DictReader(dosya)
#     for satir in okuyucu:
#         if int(satir['yas'])>25:
#             print(satir)
            
            
#verileri  guplama  işlemi 
from collections import defaultdict
#şehirlere göre kişi sayısını tutacak sözlük aslında bir şehirde kaç kişi olduğunu tutacak
sehirlere_gore_kisi_sayisi=defaultdict(int)
with open ('veriler.csv',mode='r',encoding='utf-8') as dosya:
    okuyucu=csv.DictReader(dosya)
    for satir in okuyucu:
        sehirlere_gore_kisi_sayisi[satir['sehir']]+=1
#sonucları yazdır 
for sehir in sehirlere_gore_kisi_sayisi.items():
    print(f"{sehir[0]} şehrinde {sehir[1]} kişi var")