n = int(input("Nhap n: "))

count = 1
print(n, end=" ")

while n != 1:
    if n % 2 == 0:
        n = n // 2
    else:
        n = 3*n + 1

    print(n, end=" ")
    count += 1

print("\nHailstones sinh duoc:", count)
