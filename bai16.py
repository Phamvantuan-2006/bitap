import calendar

year = int(input("Nhap nam (>1582): "))

for m in range(1,13):
    print("\nThang", m)
    print(calendar.month(year, m))
