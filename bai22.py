n = int(input("Nhap n: "))

count = 0
total = 0

print("Cac uoc so:", end=" ")

for i in range(1, n+1):
    if n % i == 0:
        print(i, end=" ")
        count += 1
        total += i

print("\nCo", count, "uoc so, tong la:", total)
