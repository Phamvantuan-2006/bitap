kw = int(input("Nhap so KW tieu thu: "))

money = 0

if kw <= 100:
    money = kw * 500

elif kw <= 250:
    money = 100*500 + (kw-100)*800

elif kw <= 350:
    money = 100*500 + 150*800 + (kw-250)*1000

else:
    money = 100*500 + 150*800 + 100*1000 + (kw-350)*1500

print("Chi phi:", money)
