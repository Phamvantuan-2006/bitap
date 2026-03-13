n = int(input("Nhap n: "))

print("Cac so hoan hao nho hon", n, ":")

for num in range(2, n):
    s = 0
    for i in range(1, num):
        if num % i == 0:
            s += i

    if s == num:
        print(num, end=" ")
