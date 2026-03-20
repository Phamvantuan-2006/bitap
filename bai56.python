# Hàm chuyển số nguyên sang nhị phân dạng 32 bit (bù 2)
def to_binary_32(n):
    # & với 0xFFFFFFFF để lấy 32 bit cuối (bù 2)
    n = n & 0xFFFFFFFF
    
    binary = ""
    
    # Duyệt 32 bit
    for i in range(31, -1, -1):
        # Lấy từng bit bằng dịch phải và AND
        bit = (n >> i) & 1
        binary += str(bit)
        
        # Thêm khoảng trắng mỗi 8 bit cho dễ nhìn
        if i % 8 == 0:
            binary += " "
    
    return binary.strip()


# Hàm chuyển sang hệ 16 (hex)
def to_hex(n):
    # & để đảm bảo dạng 32 bit
    return hex(n & 0xFFFFFFFF)[2:].upper()


# Chương trình chính
n = int(input("Nhap n: "))

# In số thập phân
print(n)

# In nhị phân
print("Binary:", to_binary_32(n))

# In hệ 16
print("Hex:", to_hex(n))
