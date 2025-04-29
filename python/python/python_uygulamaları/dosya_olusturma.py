# dosya=open("deneme.txt","w")

# dosya.close()

# dosya=open("deneme.txt","r")

# veri=dosya.read()

# print(veri)  "a" ekleme anlamına geilyor 

# dosya=open("deneme.txt","a",encoding="utf-8")

# eklencek_veri="\nhayat sevince  güzel "
# eklencek_veri=dosya.readlines()#liste şeklinde  okur 
# del eklencek_veri[0]#silme işlemi 
# dosya.write(eklencek_veri)
# dosya.close()


dosya=open("deneme.txt","x+",encoding="utf-8")#hem dosya açamaya  hemde okumaya yarar ancak boyle bir dosyanız varsa hat a verir 