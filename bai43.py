n = int(input("Nhap n (<40): "))

f1 = 1
f2 = 1

if n == 1 or n == 2:
    fn = 1
else:
    for i in range(3, n+1):
        fn = f1 + f2
        f1 = f2
        f2 = fn

print("F(",n,") =",fn)
