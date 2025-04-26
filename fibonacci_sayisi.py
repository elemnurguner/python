def fibonacci_serisi(sinir):
    #fibonacci serisinin ilk iki elemanı 
    fib_serisi=[0,1]
    while fib_serisi[-1]+fib_serisi[-2] <= sinir:
        fib_serisi.append(fib_serisi[-1]+fib_serisi[-2])
        
    return fib_serisi
#kullanıcıdan bir sınır sayısı değeri alalım
try:
    sinir = int(input("Fibonnacci serisi için bir sınır serisi değeri girin:"))
    if sinir <0:
        print("Lütfen pozitif bir sayı girin.")
    else:
        seri=fibonacci_serisi(sinir)
        print(f"{sinir} değerine kadar olan fibonacci serisi: {seri}"),
except ValueError:
    print("Geçersiz giriş!Lütfen pozitif bir sayı girin.")
        
    