import requests

def hava_durumu_bilgisi(latitude, longitude):
    url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true"
    
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        sicaklik = data['current_weather']['temperature']
        ruzgar_hizi = data['current_weather']['windspeed']
        hava_durumu_kodu = data['current_weather']['weathercode']
        
        # Hava durumu kodunu açıklamaya çevirme
        hava_durumu = hava_durumu_aciklamasi(hava_durumu_kodu)
        
        print(f"Hava durumu bilgileri:")
        print(f"- Sıcaklık: {sicaklik}°C")
        print(f"- Rüzgar Hızı: {ruzgar_hizi} km/s")
        print(f"- Hava Durumu: {hava_durumu}")
    else:
        print(f"Hata: {response.status_code}")

def hava_durumu_aciklamasi(kod):
    # Hava durumu kodlarını açıklamaya çevirme
    hava_durumu_sozluk = {
        0: "Açık",
        1: "Çoğunlukla açık",
        2: "Parçalı bulutlu",
        3: "Kapalı",
        45: "Sis",
        48: "Don sisi",
        51: "Hafif çisenti",
        53: "Orta şiddetli çisenti",
        55: "Yoğun çisenti",
        56: "Hafif donan çisenti",
        57: "Yoğun donan çisenti",
        61: "Hafif yağmur",
        63: "Orta şiddetli yağmur",
        65: "Yoğun yağmur",
        66: "Hafif donan yağmur",
        67: "Yoğun donan yağmur",
        71: "Hafif kar",
        73: "Orta şiddetli kar",
        75: "Yoğun kar",
        77: "Kar taneleri",
        80: "Hafif sağanak yağmur",
        81: "Orta şiddetli sağanak yağmur",
        82: "Yoğun sağanak yağmur",
        85: "Hafif kar sağanağı",
        86: "Yoğun kar sağanağı",
        95: "Fırtına",
        96: "Hafif dolu fırtınası",
        99: "Yoğun dolu fırtınası"
    }
    return hava_durumu_sozluk.get(kod, "Bilinmeyen hava durumu")

if __name__ == "__main__":
    # İstanbul için enlem ve boylam
    latitude = 41.01
    longitude = 28.98
    
    hava_durumu_bilgisi(latitude, longitude), 28.8742251703339