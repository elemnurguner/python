#haftanın  gününü söyleyen program
from datetime import datetime

def  haftanın_gununu_bul(tarih):
    #haftanın gunnlerini liste olrak tanımlayalım 
    gunler=["Pazartesi","Salı","Çarşamba","Perşembe","Cuma","Cumartesi","Pazar"]
    
    #verilen tarihin haftanın  kaçıncı gunu oldugunu  bulalım
    gun_indeksi=tarih.weekday()
    #haftanın gununu  dondur 
    return gunler[gun_indeksi]
#kullanıcıdan tarih alalım
tarih=input("Tarih giriniz YYYY-AA-GG formatında:")
# String'i datetime nesnesine çevirelim
tarih = datetime.strptime(tarih, "%Y-%m-%d")
#haftanın gununu  bul ve ekrana yazdır
print(f"{tarih} tarihi {haftanın_gununu_bul(tarih)} günüdür.")
    