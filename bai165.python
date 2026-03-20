import math

class PhanSo:
    def __init__(self, tu, mau):
        self.tu = tu
        self.mau = mau

    # Rút gọn phân số
    def rut_gon(self):
        ucln = math.gcd(self.tu, self.mau)
        self.tu //= ucln
        self.mau //= ucln

    # Hiển thị
    def hien_thi(self):
        self.rut_gon()
        return f"{self.tu}/{self.mau}"

    # Cộng
    def cong(self, other):
        tu = self.tu * other.mau + other.tu * self.mau
        mau = self.mau * other.mau
        return PhanSo(tu, mau)

    # Trừ
    def tru(self, other):
        tu = self.tu * other.mau - other.tu * self.mau
        mau = self.mau * other.mau
        return PhanSo(tu, mau)

    # Nhân
    def nhan(self, other):
        return PhanSo(self.tu * other.tu, self.mau * other.mau)

    # Chia
    def chia(self, other):
        return PhanSo(self.tu * other.mau, self.mau * other.tu)


# Nhập dữ liệu
a_tu, a_mau = map(int, input("Nhap tu so va mau so a: ").split())
b_tu, b_mau = map(int, input("Nhap tu so va mau so b: ").split())

a = PhanSo(a_tu, a_mau)
b = PhanSo(b_tu, b_mau)

# Tính toán
print("a + b =", a.cong(b).hien_thi())
print("a - b =", a.tru(b).hien_thi())
print("a * b =", a.nhan(b).hien_thi())
print("a / b =", a.chia(b).hien_thi())
