print("So Armstrong co 3, 4 chu so:")

for num in range(100,10000):

    temp = num
    digits = []
    
    while temp > 0:
        digits.append(temp % 10)
        temp //= 10
    
    power = len(digits)

    s = 0
    for d in digits:
        s += d ** power

    if s == num:
        print(num, end=" ")
