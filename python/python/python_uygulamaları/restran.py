

masalar=dict()

for a in range(20):
    masalar[a]=0
    
def hesapekle():
    masa_no =int(input("masa  numarası :"))
    bakiye =masalar[masa_no]
    eklenecek_ucret=float(input("Eklenecek ücret :"))
    guncel_bakiye= bakiye+eklenecek_ucret
    masalar[masa_no]= guncel_bakiye
    print("işleminizz  tamamlandı ")

def hesap_odeme():
    masa_no =int(input("masa  numarası :"))
    bakiye =masalar[masa_no]
    print("Masa {}'in hesabı {} TL".format(masa_no,bakiye))
    masalar[masa_no]=0
    print("hesap ödendi ")

def dosya_kontrolu(dosya_adi):
    try:
        dosya =open(dosya_adi,"r",encoding="utf-8")
        veri =dosya.read()
        veri=veri.split("\n")
        veri.pop()
        dosya.close()
        for a in enumerate(veri):
            masalar[a[0]]= float(a[1])
    except FileNotFoundError:
        dosya = open(dosya_adi,"w",encoding="utf-8")
        dosya.close()
        print("kayıt  dosyası oluşturuldus")
    
def dosya_guncelle(dosya_adi):
    dosya = open(dosya_adi,"w",encoding="utf-8")
    for a in range(20):
        bakiye =masalar[a]
        bakiye =str(bakiye)
        dosya.write(bakiye+"\n")
    dosya.close()
    
    
        
def ana_islemler():
    dosya_kontrolu("bakiye.txt")
    print ("""
           Elemnur Güner Restoran Uygulaması 
           1-Masaları görümtüle  
           2-Hesap ekle 
           3-Hesap Ödeme 
           q-Çıkış
           
           
           """)
    secim =input("Yapılacak işlemleri   giriniz:")
    if secim == "1":
        for a in range(20):
            print("Masa  {} icin hesap :{}".format(a,masalar[a]))
    elif secim== "2":
        hesapekle()
    elif secim=="3":
        hesap_odeme()
    elif secim=="q" or secim=="Q":
        print("Çıkış yapılıyor iyi günler  ")
        quit()
    else:
        print("Hatalı seçim yaptınız")
        dosya_guncelle("bakiye.txt")
    input("Ana  menuye  donmek için entera  basınız .")
    
ana_islemler()