n = int(input("Nhap so tien (nghin dong): "))

best = None

for a in range(n//5 + 1):      # 5000
    for b in range(n//2 + 1):  # 2000
        for c in range(n + 1): # 1000
            
            if 5*a + 2*b + c == n:
                total = a + b + c
                
                if b <= total/2:
                    if best is None or b < best[1]:
                        best = (a,b,c)

if best:
    print("5000:",best[0])
    print("2000:",best[1])
    print("1000:",best[2])
else:
    print("Khong tim duoc cach doi")
