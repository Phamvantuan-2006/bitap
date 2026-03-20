import random

# Nhập bậc ma trận
n = int(input("Nhap bac ma tran: "))

# a. Tạo ma trận vuông n x n với giá trị ngẫu nhiên [-10, 10]
A = []
for i in range(n):
    row = []
    for j in range(n):
        row.append(random.randint(-10, 10))
    A.append(row)

# In ma trận
print("Ma tran:")
for row in A:
    print(*row)


# b. Tìm điểm yên ngựa
for i in range(n):
    for j in range(n):
        x = A[i][j]

        # Kiểm tra điều kiện 1:
        # x là MIN của dòng i và MAX của cột j
        if x == min(A[i]) and x == max(A[k][j] for k in range(n)):
            print(f"MIN dong MAX cot: a[{i}][{j}] = {x}")

        # Kiểm tra điều kiện 2:
        # x là MAX của dòng i và MIN của cột j
        if x == max(A[i]) and x == min(A[k][j] for k in range(n)):
            print(f"MAX dong MIN cot: a[{i}][{j}] = {x}")
