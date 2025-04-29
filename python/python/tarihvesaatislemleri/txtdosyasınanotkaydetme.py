#dosya adını belirleyelim  
dosya_adi="notlar.txt"
#kullanıcıdan  not al
not_metni=input("notunuzu girin")

#dosyayı aç ve  notu ekle
with open(dosya_adi,"a",encoding="utf-8") as dosya:
    dosya.write(not_metni+"\n")
print("Notunuzu başarıyla kaydedildi ")