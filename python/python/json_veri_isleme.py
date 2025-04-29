import json


# JSON verisi
# json_veri = '''
# {
#   "isim": "Ahmet",
#   "yas": 30,
#   "meslek": "Mühendis",
#   "beceriler": ["Python", "JavaScript", "SQL"],
#   "projeler": [
#     {"isim": "Proje 1", "durum": "Tamamlandı"},
#     {"isim": "Proje 2", "durum": "Devam Ediyor"}
#   ]
# }'''

#json verisini python sözlüğüne dönüştrüme
# veri=json.loads(json_veri)
#veriyi isleme 
# print(f"İsim: {veri['isim']}")
# print(f"Yaş: {veri['yas']}")
# print(f"Meslek: {veri['meslek']}")
# print("Beceriler:")
# for beceri in veri['beceriler']:
#     print(f"- {beceri}")
    
# print("Projeler:")
# for proje in veri['projeler']:
#     print(f"- {proje['isim']} ({proje['durum']})")
    
    
#json dosyasından veri okuma 
with open('json_veri.json',mode='r',encoding='utf-8') as dosya:
    veri=json.load(dosya)
    
#veri işleme 
print(f"İsim: {veri['isim']}")
print(f"Yaş: {veri['yas']}")
print(f"Meslek: {veri['meslek']}")