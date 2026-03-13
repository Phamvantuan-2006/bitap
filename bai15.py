day = int(input("Nhap ngay: "))
month = int(input("Nhap thang: "))
year = int(input("Nhap nam: "))

leap = (year%4==0 and year%100!=0) or (year%400==0)

days = [31,29 if leap else 28,31,30,31,30,31,31,30,31,30,31]

sum_day = day

for i in range(month-1):
    sum_day += days[i]

print("Ngay thu:", sum_day)
