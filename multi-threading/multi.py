import threading
import time
import queue

# Siparişlerin tutulacağı bir kuyruk (queue) oluşturuyoruz.
siparis_kuyrugu = queue.Queue()

# Sipariş alan fonksiyon
def siparis_al():
    for i in range(1, 6):  # 5 sipariş alacağız
        print(f"Sipariş {i} alındı.")
        siparis_kuyrugu.put(f"Sipariş {i}")  # Siparişi kuyruğa ekle
        time.sleep(1)  # Sipariş almak 1 saniye sürsün

# Sipariş hazırlayan fonksiyon
def siparis_hazirla():
    while not siparis_kuyrugu.empty():  # Kuyruk boş değilse çalış
        siparis = siparis_kuyrugu.get()  # Siparişi kuyruktan al
        print(f"{siparis} hazırlanıyor...")
        time.sleep(2)  # Siparişi hazırlamak 2 saniye sürsün
        print(f"{siparis} hazırlandı!")
        siparis_kuyrugu.task_done()  # Siparişin hazırlandığını bildir

# Thread'leri oluştur
siparis_al_thread = threading.Thread(target=siparis_al)
siparis_hazirla_thread = threading.Thread(target=siparis_hazirla)

# Thread'leri başlat
siparis_al_thread.start()
time.sleep(0.5)  # Sipariş alan thread'in biraz önde başlamasını sağla
siparis_hazirla_thread.start()

# Thread'lerin bitmesini bekle
siparis_al_thread.join()
siparis_hazirla_thread.join()

print("Tüm siparişler tamamlandı!")