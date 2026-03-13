d = int(input("Nhap ngay: "))
m = int(input("Nhap thang: "))
y = int(input("Nhap nam: "))

# kiểm tra năm nhuận
leap = False
if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0):
    leap = True

# số ngày trong tháng
days = [31,29 if leap else 28,31,30,31,30,31,31,30,31,30,31]

if m < 1 or m > 12 or d < 1 or d > days[m-1]:
    print("Ngay khong hop le")
else:
    print("Hop le")

    a = (14 - m) // 12
    y2 = y - a
    m2 = m + 12*a - 2

    day = (d + y2 + y2//4 - y2//100 + y2//400 + (31*m2)//12) % 7

    thu = ["Chu nhat","Thu 2","Thu 3","Thu 4","Thu 5","Thu 6","Thu 7"]

    print(thu[day])
