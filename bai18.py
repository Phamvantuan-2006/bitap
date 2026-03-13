hours = int(input("Nhap so gio: "))

weeks = hours // 168
hours = hours % 168

days = hours // 24
hours = hours % 24

print(weeks,"tuan,",days,"ngay,",hours,"gio")
