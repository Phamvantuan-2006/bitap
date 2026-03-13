while True:
    sin = input("SIN (0 de thoat): ")

    if sin == "0":
        break

    if len(sin) != 9 or not sin.isdigit():
        print("SIN khong hop le!")
        continue

    s1 = 0
    s2 = 0

    for i in range(0, 9, 2):
        s1 += int(sin[i])

    for i in range(1, 9, 2):
        x = int(sin[i]) * 2
        if x >= 10:
            x = x//10 + x%10
        s2 += x

    tong = s1 + s2

    if tong % 10 == 0:
        print("SIN hop le!")
    else:
        print("SIN khong hop le!")
