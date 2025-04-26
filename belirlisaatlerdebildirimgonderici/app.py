import tkinter as tk
from tkinter import messagebox
from plyer import notification
import time
from threading import Thread

class BildirimUygulamasi:
    def __init__(self, root):
        self.root = root
        self.root.title("Bildirim Gönderici")
        self.root.geometry("300x200")

        self.label = tk.Label(root, text="Bildirim Saati (HH:MM):")
        self.label.pack(pady=10)

        self.entry = tk.Entry(root)
        self.entry.pack(pady=10)

        self.button = tk.Button(root, text="Bildirimi Ayarla", command=self.bildirimi_ayarla)
        self.button.pack(pady=20)

    def bildirimi_ayarla(self):
        saat = self.entry.get()
        try:
            bildirim_saati = time.strptime(saat, "%H:%M")
            Thread(target=self.bildirim_gonder, args=(bildirim_saati,)).start()
            messagebox.showinfo("Başarılı", f"Bildirim {saat} için ayarlandı.")
        except ValueError:
            messagebox.showerror("Hata", "Lütfen geçerli bir saat formatı girin (HH:MM).")

    def bildirim_gonder(self, bildirim_saati):
        while True:
            suanki_zaman = time.localtime()
            if suanki_zaman.tm_hour == bildirim_saati.tm_hour and suanki_zaman.tm_min == bildirim_saati.tm_min:
                notification.notify(
                    title="Bildirim",
                    message="SELAM GÜZEL KADIN!",
                    timeout=10
                )
                break
            time.sleep(30)  # Her 30 saniyede bir kontrol et

if __name__ == "__main__":
    root = tk.Tk()
    uygulama = BildirimUygulamasi(root)
    root.mainloop()