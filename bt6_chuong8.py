def tinh_tien_cuoc(loai_xe, so_km, thoi_gian_cho):
    if loai_xe == 4:
        gia_mo_cua = 11.000
        gia_trong_pham_vi = 12.100
        gia_ngoai_pham_vi = 10.000
    elif loai_xe == 7:
        gia_mo_cua = 13000
        gia_trong_pham_vi = 14.100
        gia_ngoai_pham_vi = 12.000
    else:
        return "Loại xe không hợp lệ"

    km_dau_tien = 0.8
    km_trong_pham_vi = min(so_km, 20)
    km_ngoai_pham_vi = max(0, so_km - 20)

    tien_di_chuyen = gia_mo_cua + km_trong_pham_vi * gia_trong_pham_vi + km_ngoai_pham_vi * gia_ngoai_pham_vi

    tien_cho = max(0, thoi_gian_cho - 5) * 800 
     # Tiền chờ từ phút thứ 6 trở đi

    tien_cuoc = tien_di_chuyen + tien_cho

    return (f"Tiền chờ: {tien_cho} đồng\Tiền di chuyển: {tien_di_chuyen} đồng\Tiền cước: {tien_cuoc} đồng")

# nhập 
loai_xe = int(input("Nhập loại xe (4 hoặc 7): "))
so_km = float(input("Nhập số km: "))
thoi_gian_cho = int(input("Nhập thời gian chờ (phút): "))

print(tinh_tien_cuoc(loai_xe, so_km, thoi_gian_cho))