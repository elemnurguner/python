import requests

# SpaceX API endpoint'i (Son görevler)
url = "https://api.spacexdata.com/v4/launches/latest"

# API'ye istek gönder
response = requests.get(url)

# Eğer istek başarılı ise
if response.status_code == 200:
    data = response.json()
    print("Son SpaceX Görevi:", data['name'])
    print("Detaylar:", data['details'])
else:
    print(f"API isteği başarısız oldu. Hata kodu: {response.status_code}")