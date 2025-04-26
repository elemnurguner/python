import random
tutulan_sayi = random.randint(1, 100)
tahmin_hakki=10

print("1 ile 100 arası sayı tuutum.Tahmin etmeyeçalışın")

#kullanıcının tahminlerini almaya çalışalım 
for deneme in range(tahmin_hakki):
    tahmin=int(input(f"{deneme+1}. tahmininizi giriniz: "))#kullanıcıdan tahmin alalım
    
    if tahmin < tutulan_sayi:
        print("Daha büyük bir sayı giriniz")
    elif tahmin > tutulan_sayi:
        print("Daha küçük bir sayı giriniz")
    else:
        print(f"Tebrikler!{tutulan_sayi}sayisinı {deneme+1}denemede buldunuz")
        break
else:
    print(f"maalesef,tahmin hakkınız bitti.Tutulan sayi{tutulan_sayi}idi")