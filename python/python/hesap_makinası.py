#ilk olrak kullanıcıdan iki sayı ve bir işlem alalım 
sayi1=float(input("Birinci sayıyı giriniz: "))
sayi2=float(input("İkinci sayıyı giriniz: "))
islem=input("İşlemi giriniz:*,-,+,/ : ")

if islem=="+":
   sonuc =sayi1+sayi2
elif islem=="-":
    sonuc=sayi1-sayi2
elif islem=="*":
    sonuc=sayi1*sayi2
elif islem=="/":
    if sayi2!=0:
     sonuc=sayi1/sayi2
    else:
        sonuc="Sıfıra bölme hatası"
else:
    sonuc="Geçersiz işlem"
print("Sonuc: ",sonuc)
