# Hàm chuẩn hóa chuỗi: bỏ khoảng trắng và chuyển về chữ thường
def chuan_hoa(s):
    return "".join(s.lower().split())


# a. Kiểm tra chuỗi đối xứng (palindrome)
def la_doi_xung(s):
    s = chuan_hoa(s)   # chuẩn hóa trước
    return s == s[::-1]  # so sánh với chuỗi đảo


# b. Xóa tất cả ký tự xuất hiện trong chuỗi thứ 2 khỏi chuỗi ban đầu
def xoa_ky_tu(s, remove):
    result = ""
    remove = remove.lower()  # không phân biệt hoa thường

    for ch in s:
        if ch.lower() not in remove:
            result += ch  # giữ lại ký tự

    return result


# ===== Chương trình chính =====
s = input("Nhap chuoi: ")

# Kiểm tra đối xứng
if la_doi_xung(s):
    print("Chuoi doi xung")
else:
    print("Chuoi khong doi xung")

# Nhập chuỗi cần xóa
remove = input("Xoa ky tu nao: ")

# Xóa ký tự
ket_qua = xoa_ky_tu(s, remove)

print(ket_qua)
