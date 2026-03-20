import random

# Nhập số lượng phần tử
n = int(input("Nhap n: "))

# Tạo mảng ngẫu nhiên trong [-100, 100]
arr = [random.randint(-100, 100) for _ in range(n)]

# In mảng ban đầu
print("Mang ban dau:")
print(*arr)


# Tách các phần tử
le = []    # số lẻ
chan = []  # số chẵn
zero = []  # số 0

for x in arr:
    if x == 0:
        zero.append(x)
    elif x % 2 == 0:
        chan.append(x)
    else:
        le.append(x)

# Ghép lại theo yêu cầu:
# lẻ (đầu) + 0 (giữa) + chẵn (cuối)
ket_qua = le + zero + chan

# In kết quả
print("Mang sau khi sap xep:")
print(*ket_qua)
