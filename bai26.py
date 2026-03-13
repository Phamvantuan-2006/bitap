a = int(input("Nhap tu so: "))
b = int(input("Nhap mau so: "))

# tìm USCLN
x, y = abs(a), abs(b)
while y != 0:
    x, y = y, x % y

gcd = x

a //= gcd
b //= gcd

if b < 0:
    a = -a
    b = -b

if b == 1:
    print("Rut gon:", a)
else:
    print("Rut gon:", a, "/", b)
