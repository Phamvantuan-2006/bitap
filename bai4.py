import math

a = float(input("Nhap canh a: "))
b = float(input("Nhap canh b: "))
c = float(input("Nhap canh c: "))

if a + b > c and a + c > b and b + c > a:
    
    if a*a + b*b == c*c or a*a + c*c == b*b or b*b + c*c == a*a:
        print("Tam giac vuong")
    elif a == b == c:
        print("Tam giac deu")
    elif a == b or a == c or b == c:
        print("Tam giac can")
    else:
        print("Tam giac thuong")

    p = (a + b + c) / 2
    S = math.sqrt(p * (p - a) * (p - b) * (p - c))
    
    print("Dien tich S =", S)

else:
    print("3 canh khong tao thanh tam giac")
