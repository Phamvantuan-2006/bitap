import math

def dientich(x1, y1, x2, y2, x3, y3):
    return abs((x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2)) / 2)

# Nhập tọa độ
xA = float(input("Nhap xA: "))
yA = float(input("Nhap yA: "))

xB = float(input("Nhap xB: "))
yB = float(input("Nhap yB: "))

xC = float(input("Nhap xC: "))
yC = float(input("Nhap yC: "))

xM = float(input("Nhap xM: "))
yM = float(input("Nhap yM: "))

# Tính diện tích
SABC = dientich(xA,yA,xB,yB,xC,yC)
SMAB = dientich(xM,yM,xA,yA,xB,yB)
SMBC = dientich(xM,yM,xB,yB,xC,yC)
SMCA = dientich(xM,yM,xC,yC,xA,yA)

if abs(SMAB + SMBC + SMCA - SABC) < 1e-6:
    if SMAB == 0 or SMBC == 0 or SMCA == 0:
        print("M nam tren canh tam giac ABC")
    else:
        print("M nam trong tam giac ABC")
else:
    print("M nam ngoai tam giac ABC")
