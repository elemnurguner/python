import os

def dosyaayiklama(directory,extension):
    #belirtilen dizindeki tüm dosyaları listele
    for root, dirs, files in os.walk(directory):
        for file in files:
            #dosya uzantısı belirtilen uzantı ile eşlesiyorsa
            if file.endswith(extension):
                print(os.path.join(root, file))#dosyanın  tam yolunu yazdır
            # Kullanım örneği
directory_to_search = "C:\\Users\\USER\Desktop\\acil_projeler_ysa_data\\python\\dosyaturayiklama"  # Arama yapılacak dizin
file_extension = ".txt"  # Aranacak dosya uzantısı
dosyaayiklama(directory_to_search, file_extension)  # Fonksiyonu çağır