a = int(input("Nhap a: "))
b = int(input("Nhap b: "))

# tìm USCLN bằng thuật toán Euclid
x, y = a, b
while y != 0:
    x, y = y, x % y

gcd = x
lcm = abs(a*b) // gcd

print("USCLN(a,b):", gcd)
print("BSCNN(a,b):", lcm)
