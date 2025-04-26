import json
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

#json dosyasını okurum 

with  open ("veriler.json","r",encoding="utf-8")as dosya:
    veriler =json.load(dosya)
print(veriler)


# Şehirlere göre kişi sayısını pasta grafiği ile göster
sehir_frekans = df["sehir"].value_counts()

plt.figure(figsize=(8, 8))
plt.pie(sehir_frekans, labels=sehir_frekans.index, autopct="%1.1f%%", startangle=140)
plt.title("Şehirlere Göre Kişi Dağılımı")
plt.show()