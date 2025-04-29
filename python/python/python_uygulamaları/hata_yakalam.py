a=(input("bölünen"))
b=(input("bölen"))

try:
    print ("Sonuc",float(a)/float(b))
except ValueError:
    print("lüfen geçerli bir sayı giriniz")
    
except TypeError:
    print("tip formatı hatalı")
except ZeroDivisionError:
    print("sıfıara  bolum tanımsız  olrak  geçer")

finally:
    print("Bu her zaman çalışır")

    