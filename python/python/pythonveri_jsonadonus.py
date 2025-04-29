import json
# Python sözlüğü
veri = {
    "isim": "Ahmet",
    "yas": 30,
    "meslek": "Mühendis",
    "beceriler": ["Python", "JavaScript", "SQL"],
    "projeler": [
        {"isim": "Proje 1", "durum": "Tamamlandı"},
        {"isim": "Proje 2", "durum": "Devam Ediyor"}
    ]
}

#json formatına donusturme
json_veri=json.dumps(veri,indent=4,ensure_ascii=False)
print(json_veri)

#json dosyasına yazma
with open('json_veri.json',mode='w',encoding='utf-8') as dosya:
    json.dump(veri,dosya,indent=4,ensure_ascii=False)