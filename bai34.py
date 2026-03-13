import math

a = 0
b = math.pi/2
n = 100000   # độ chính xác cao

h = (b-a)/n

s = 0.5*(math.sin(a)**2*math.cos(a) + math.sin(b)**2*math.cos(b))

for i in range(1,n):
    x = a + i*h
    s += math.sin(x)**2 * math.cos(x)

result = h * s

print("Gia tri gan dung:", result)
