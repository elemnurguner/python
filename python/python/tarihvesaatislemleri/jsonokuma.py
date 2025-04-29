import json
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

#json dosyasını okurum 

with  open ("veriler.json","r",encoding="utf-8")as dosya:
    veriler =json.load(dosya)
print(veriler)

#veri görselleştirme  için indirilmesi gerekn pip install matplotlib seaborn
#Örnek: Yaş Dağılımını Görselleştirme

#yaş verilerini çek
# yaslar=[kisi["yas"]for kisi in veriler ]
# isimler=[kisi["isim"]for kisi in veriler]

#garafik oluşturmak için
# plt.figure(figsize=(10,6))
# plt.bar(isimler,yaslar,color="skyblue")
# plt.title("kisilerin yas dagılımı")
# plt.xlabel("isim")
# plt.ylabel("yas")
# plt.show()


# Şehir verilerini çek
# sehirler = [kisi["sehir"] for kisi in veriler]

# Şehirlerin frekansını hesapla
# sehir_frekans = pd.Series(sehirler).value_counts()

# Grafik oluştur
# plt.figure(figsize=(10, 6))
# sns.barplot(x=sehir_frekans.index, y=sehir_frekans.values, palette="viridis")
# plt.title("Şehirlere Göre Kişi Sayısı")
# plt.xlabel("Şehir")
# plt.ylabel("Kişi Sayısı")
# plt.show()


import pandas as pd

# Örnek veri
veri = {
    "isim": ["Ali", "Ayşe", "Mehmet", "Zeynep", "Ahmet"],
    "yas": [25, 30, 22, 28, 35],
    "sehir": ["İstanbul", "Ankara", "İzmir", "Bursa", "İstanbul"]
}

# DataFrame oluştur
df = pd.DataFrame(veri)
print(df)

 #Örnek: Pandas ile JSON Verisini Okuma ve Görselleştirme
import pandas as pd

# JSON verisini pandas DataFrame'e dönüştür
df = pd.read_json("veriler.json")

# Veriyi görüntüle
print(df)

# Yaş dağılımını görselleştir
plt.figure(figsize=(10, 6))
sns.histplot(df["yas"], kde=True, color="blue")
plt.title("Yaş Dağılımı")
plt.xlabel("Yaş")
plt.ylabel("Frekans")
plt.show()