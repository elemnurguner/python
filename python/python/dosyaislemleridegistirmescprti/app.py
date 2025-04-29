import os

def rename_files_in_directory(directory, old_name_part, new_name_part):
    """
    Belirtilen dizindeki dosya isimlerini değiştirir.
    :param directory: Dosyaların bulunduğu dizin
    :param old_name_part: Dosya isminde değiştirilecek kısım
    :param new_name_part: Yeni dosya ismi kısmı
    """
#dizindeki tum  dosyları listele 
    for filename in os.listdir(directory):
        #dosya isminde eksik kısm varsa
        if old_name_part in filename:
            #yeni dosya ismini olustur
            new_filename = filename.replace(old_name_part, new_name_part)
            #eski ve yeni dosya yapılarını oluştur 
            old_path = os.path.join(directory, filename)
            new_path = os.path.join(directory, new_filename)
            #dosya ismini degistir
            os.rename(old_path, new_path)
            print(f"{filename} dosyasının adı {new_filename} olarak değiştirildi.")

# Kullanım örneği
directory_path = "C:\\Users\\USER\\Desktop\\acil_projeler_ysa_data\python\\dosyaislemleridegistirmescprti"  # Dosyaların bulunduğu dizin
old_text = "dunya"  # Dosya isminde değiştirilecek kısım
new_text = "cehennem"  # Yeni dosya ismi kısmı

rename_files_in_directory(directory_path, old_text, new_text)