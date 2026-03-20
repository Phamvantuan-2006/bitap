def neg_average(arr, n, i=0, tong=0, dem=0):
    # Điều kiện dừng
    if i == n:
        if dem == 0:
            return 0  # không có số âm
        return tong / dem
    
    # Nếu là số âm
    if arr[i] < 0:
        tong += arr[i]
        dem += 1
    
    # Gọi đệ quy
    return neg_average(arr, n, i + 1, tong, dem)


# Test
a = [-2, 3, -4, 5, 6, -8]
n = len(a)

print("Trung binh cong cac phan tu am:", neg_average(a, n))
