import sqlite3

#db ye baglan 
conn=sqlite3.connect('ornek.db')

#cursor nesnesi olustur 
cursor=conn.cursor()

#tablo olustur 
create_table_query='''
CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ad TEXT NOT NULL,   
    soyad TEXT NOT NULL,
    yas INTEGER NOT NULL
    );

'''
cursor.execute(create_table_query)
conn.commit()

#VERİ EKLİYORUZ
insert_query='''
INSERT INTO users(ad,soyad,yas) VALUES(?,?,?);

'''
cursor.execute(insert_query,('ahmet','Veli',25))
cursor.execute(insert_query,('selçuk','Fatma',30))
conn.commit()
print('Ekleme işlemi başarılı')

#veri güncelleme
update_query='''
UPDATE users
SET yas=?
WHERE ad =?;
'''
cursor.execute(update_query,(38,'Ali'))
conn.commit()
print('Güncelleme işlemi başarılı')

#veri silme
delete_query='''DELETE FROM users WHERE ad=?;'''
cursor.execute(delete_query,('Ali',))
conn.commit()
print('Silme işlemi başarılı')

#veri listeleme

# Verileri sorgula
select_query = '''
SELECT * FROM users;
'''
cursor.execute(select_query)

# Tüm satırları al
rows = cursor.fetchall()

# Sonuçları ekrana yazdır
print("ID | Ad    | Soyad   | Yaş")
print("---------------------------")
for row in rows:
    print(f"{row[0]}  | {row[1]} | {row[2]} | {row[3]}")
    print("-----------listeleme işlemi başarılı ----------------")

conn.close()


