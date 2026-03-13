day = int(input("Nhap ngay: "))
month = int(input("Nhap thang: "))
year = int(input("Nhap nam: "))

# kiểm tra năm nhuận
leap = (year%4==0 and year%100!=0) or (year%400==0)

days = [31,29 if leap else 28,31,30,31,30,31,31,30,31,30,31]

# ngày tiếp theo
n_day = day + 1
n_month = month
n_year = year

if n_day > days[month-1]:
    n_day = 1
    n_month += 1
    if n_month > 12:
        n_month = 1
        n_year += 1

print("Ngay mai:", n_day,"/",n_month,"/",n_year)

# ngày hôm qua
p_day = day - 1
p_month = month
p_year = year

if p_day == 0:
    p_month -= 1
    if p_month == 0:
        p_month = 12
        p_year -= 1

    leap = (p_year%4==0 and p_year%100!=0) or (p_year%400==0)
    days = [31,29 if leap else 28,31,30,31,30,31,31,30,31,30,31]

    p_day = days[p_month-1]

print("Hom qua:", p_day,"/",p_month,"/",p_year)
