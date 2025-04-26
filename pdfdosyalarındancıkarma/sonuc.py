import pdfplumber

# PDF dosyasını açma
pdf_dosya_adi = "dummy.pdf"
with pdfplumber.open(pdf_dosya_adi) as pdf:
    # PDF dosyasındaki sayfa sayısını öğrenme
    sayfa_sayisi = len(pdf.pages)
    print(f"Toplam sayfa sayısı: {sayfa_sayisi}")

    # Her bir sayfadaki metni çıkarma
    for sayfa_num in range(sayfa_sayisi):
        sayfa = pdf.pages[sayfa_num]
        print(f"Sayfa {sayfa_num + 1}:")

        # Metin çıkarma
        metin = sayfa.extract_text()
        if metin:
            print(metin)
        else:
            print("Bu sayfada metin bulunamadı.")

        # Kelimeleri çıkarma
        kelimeler = sayfa.extract_words()
        if kelimeler:
            print("Kelimeler:", kelimeler)
        else:
            print("Bu sayfada kelime bulunamadı.")