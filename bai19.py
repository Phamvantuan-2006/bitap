h1 = int(input("Nhap gio [1]: "))
m1 = int(input("Nhap phut [1]: "))
s1 = int(input("Nhap giay [1]: "))

h2 = int(input("Nhap gio [2]: "))
m2 = int(input("Nhap phut [2]: "))
s2 = int(input("Nhap giay [2]: "))

t1 = h1*3600 + m1*60 + s1
t2 = h2*3600 + m2*60 + s2

diff = abs(t2 - t1)

h = diff // 3600
diff %= 3600
m = diff // 60
s = diff % 60

print("Hieu thoi gian:", h, "gio", m, "phut", s, "giay")
