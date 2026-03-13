cut = float(input("Nhap diem chuan: "))

d1 = float(input("Nhap diem mon 1: "))
d2 = float(input("Nhap diem mon 2: "))
d3 = float(input("Nhap diem mon 3: "))

kv = input("Nhap khu vuc (A,B,C,X): ")
dt = int(input("Nhap doi tuong (1,2,3,0): "))

bonus = 0

if kv == "A":
    bonus += 2
elif kv == "B":
    bonus += 1
elif kv == "C":
    bonus += 0.5

if dt == 1:
    bonus += 2.5
elif dt == 2:
    bonus += 1.5
elif dt == 3:
    bonus += 1

total = d1 + d2 + d3 + bonus

if d1==0 or d2==0 or d3==0:
    print("Rot")
elif total >= cut:
    print("Dau")
else:
    print("Rot")

print("Tong diem:", total)
