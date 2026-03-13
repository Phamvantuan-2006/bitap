names = ["A","B","C","D","E"]

year = int(input("Nhap nam: "))
start = int(input("Nhap thu cho ngay dau tien cua nam (0=CN): "))
month = int(input("Nhap thang: "))

import calendar

days = calendar.monthrange(year,month)[1]

print("\nSun Mon Tue Wed Thu Fri Sat")

pos = start
for i in range(pos):
    print("    ",end="")

for d in range(1,days+1):

    person = names[(d-1)%5]

    print(f"{d:2}[{person}]",end=" ")

    pos+=1
    if pos%7==0:
        print()

print()
