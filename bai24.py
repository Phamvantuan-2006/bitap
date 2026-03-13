n = int(input("Nhap n: "))

# a. số chữ số
count = len(str(n))
print(count, "chu so")

# b. chữ số cuối
print("Chu so cuoi cung la:", n % 10)

# c. chữ số đầu
first = int(str(n)[0])
print("Chu so dau tien la:", first)

# d. tổng các chữ số
s = 0
temp = n
while temp > 0:
    s += temp % 10
    temp //= 10

print("Tong cac chu so la:", s)

# e. đảo ngược số
rev = 0
temp = n
while temp > 0:
    rev = rev*10 + temp%10
    temp //= 10

print("So dao nguoc la:", rev)
