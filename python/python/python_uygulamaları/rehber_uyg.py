rehber ={
    
    "Battal":{
        
    "Cep":12323125656,
    "iş":56454565456,
    "Ev":56666666666
    }
    ,
    "Ayse":{
        
    "Cep":12323125656,
    "iş":56454565456,
    "Ev":56666666666
    },
    
    "Fatma":{
        
    "Cep":12323125656,
    "iş":56454565456,
    "Ev":56666666666
    }
}

while True:
    isimler = rehber.keys()
    giris =input("Kişi adı:")
    
    #verilere ulaşmak iiçn get metodu kullandık ilki rehberden gelen   ikincisi   inputa girilern 
    if giris in isimler:
        tel =input("istediğiniz  telefon nosu hangisidir:")
        print(rehber.get(giris).get(tel,"istediğiniz numara mevcut  değildir."))
    else :
        print("istediğiniz  kişi mevcut değil")
        cikis =input("Yeniden arama yapmak için enter a  basınız  yada  çıkış yapmak için Q tuşuna basıp enterlayınız.")
        if cikis =='Q' or cikis=='q':
            print("cikiş yapılıyor")
            quit()