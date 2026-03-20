# Nhập tên file cần đọc
filename = input("Nhap ten file: ")

try:
    # Mở file ở chế độ đọc
    with open(filename, "r", encoding="utf-8") as f:
        lines = f.readlines()  # Đọc toàn bộ dòng trong file

    total_lines = len(lines)  # Tổng số dòng
    page_size = 25           # Mỗi trang 25 dòng

    # Duyệt từng trang
    for i in range(0, total_lines, page_size):
        # Lấy 25 dòng cho mỗi lần hiển thị
        page = lines[i:i + page_size]

        # In từng dòng ra màn hình
        for line in page:
            print(line, end="")  # end="" để không bị xuống dòng 2 lần

        # Nếu chưa phải trang cuối thì dừng chờ Enter
        if i + page_size < total_lines:
            input("\n--- Nhan Enter de xem tiep ---")

    print("\n--- Het file ---")

except FileNotFoundError:
    print("Khong tim thay file!")
