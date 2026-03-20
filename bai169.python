def tinh_tien(vao_h, vao_m, ra_h, ra_m):
    vao = vao_h * 60 + vao_m
    ra = ra_h * 60 + ra_m

    # Nếu qua ngày (vd: 22h -> 2h)
    if ra < vao:
        ra += 24 * 60

    tong_tien = 0

    for t in range(vao, ra):
        gio = (t // 60) % 24

        if 6 <= gio < 18:
            tong_tien += 10000 / 60
        else:
            tong_tien += 15000 / 60

    return int(tong_tien)


def hop_le(vao, ra):
    vao_phut = vao[0] * 60 + vao[1]
    ra_phut = ra[0] * 60 + ra[1]

    if ra_phut < vao_phut:
        ra_phut += 24 * 60

    # Không quá 12 giờ (2 ca)
    return (ra_phut - vao_phut) <= 12 * 60


# Chương trình chính
n = int(input("Nhap so cong nhan: "))

for _ in range(n):
    id_cn = input("Nhap ID cong nhan: ")

    vao_h, vao_m = map(int, input("Vao (gio phut): ").split())
    ra_h, ra_m = map(int, input("Ra (gio phut): ").split())

    if not hop_le((vao_h, vao_m), (ra_h, ra_m)):
        print(id_cn, "Nhap sai!")
        continue

    tien = tinh_tien(vao_h, vao_m, ra_h, ra_m)

    print(id_cn,
          f"{vao_h:02d}:{vao_m:02d}",
          f"{ra_h:02d}:{ra_m:02d}",
          tien)
