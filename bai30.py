r = float(input("Nhap lai suat: "))
p = float(input("Nhap von ban dau: "))
n = int(input("Nhap thoi han (nam): "))

print("\nLai suat:", r*100, "%")
print("Von ban dau:", p)
print("Thoi han:", n, "nam")

print("\nNam   Von")

for i in range(1, n+1):
    amount = p * (1 + r) ** i
    print(i, "   ", round(amount,2))
