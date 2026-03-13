import math

n = int(input("Nhap n: "))

def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

if is_prime(n):
    print(n, "la so nguyen to")
else:
    print(n, "khong la so nguyen to")
    
    for i in range(n-1,1,-1):
        if is_prime(i):
            print("So nguyen to be hon gan nhat:", i)
            break
