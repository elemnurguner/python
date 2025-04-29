from datetime import datetime

def yas_hesapla(dogum_yili):
    bugun = datetime.today()
    yas = bugun.year - dogum_yili.year
        
    #dogum günü henuz gelmediyse bir yaş eksilt
    if(bugun.month ,bugun.day )<(dogum_yili.month ,dogum_yili.day):
        yas -= 1
    
    return yas
#ornek kullanım
dogum_yili = datetime(1990, 1, 1)
print("yaşınız",yas_hesapla(dogum_yili))
    