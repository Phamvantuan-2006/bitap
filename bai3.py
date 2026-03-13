import math

xC = float(input("Nhap toa do tam xC: "))
yC = float(input("Nhap toa do tam yC: "))
R = float(input("Nhap ban kinh R: "))

xM = float(input("Nhap xM: "))
yM = float(input("Nhap yM: "))

d = math.sqrt((xM - xC)**2 + (yM - yC)**2)

if d < R:
    print("M nam trong duong tron")
elif d == R:
    print("M nam tren duong tron")
else:
    print("M nam ngoai duong tron")
