import pyodbc

# SQL Server bağlantı dizesi
conn_str = (
    "DRIVER={SQL Server};"
    "SERVER=DESKTOP-F2T2PJU;"  # Sunucu adı
    "DATABASE=TestDB;"  # Veritabanı adı
)

# Bağlantıyı aç
conn = pyodbc.connect(conn_str)
cursor = conn.cursor()

# Kayıt ekleme sorgusu
query = "INSERT INTO Users (FirstName, LastName, Email) VALUES (?, ?, ?)"
values = ("Ahmet", "Yılmaz", "ahmet.yilmaz@example.com")

# Sorguyu çalıştır
cursor.execute(query, values)

# Değişiklikleri kaydet
conn.commit()

# Bağlantıyı kapat
cursor.close()
conn.close()

print("Kayıt başarıyla eklendi!")