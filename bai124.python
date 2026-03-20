# Hàm chuyển số nguyên -> chuỗi (integer to string)
def itos(n):
    # Nếu số là 0
    if n == 0:
        return "0"
    
    s = ""  # Chuỗi kết quả

    while n > 0:
        digit = n % 10              # Lấy chữ số cuối
        s = chr(digit + 48) + s    # Chuyển sang ký tự và ghép vào trước
        n //= 10                   # Bỏ chữ số cuối

    return s


# Hàm chuyển chuỗi -> số nguyên (string to integer)
def stoi(s):
    n = 0  # Kết quả

    for ch in s:
        digit = ord(ch) - 48   # Đổi ký tự -> số
        n = n * 10 + digit     # Nhân 10 rồi cộng chữ số

    return n


# Chương trình chính
n = int(input("Nhap so nguyen duong n: "))

# Gọi hàm itos
str_n = itos(n)
print("itos() ->", str_n)

# Gọi hàm stoi
num = stoi(str_n)
print("stoi() ->", num)
