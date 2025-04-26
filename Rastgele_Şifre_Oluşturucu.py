import random
import string

def rastgele_sifre_olustur(uzunluk):
   #şifre kullanılacak karakterler
   karakterler=string.ascii_letters+string.digits+string.punctuation
   #rastgele şifre  oluştur 
   sifre=''.join(random.choice(karakterler)for _ in range(uzunluk))
   return sifre
#kullanıcıdan şifre uzunluğunu alalım
try:
    uzunluk=int(input("Şifrenin uzunluğunu girin: "))
    if uzunluk <=0:
        print("şifre uzunluğu pozitif bir sayı olmalıdır.")
    else:
        sifre=rastgele_sifre_olustur(uzunluk)
        print(f"Oluşturulan şifre: {sifre}")
except ValueError:
    print("Geçersiz giriş!Lütfen pozitif bir sayı girin.")