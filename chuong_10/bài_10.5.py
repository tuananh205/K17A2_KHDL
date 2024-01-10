diem_quan_trong_can_kiem_tra = input("Nhập điểm quan trọng cần kiểm tra: ")
ma_buu_chinh_can_kiem_tra = input("Nhập mã bưu chính cần kiểm tra: ")

diem_quan_trong_va_ma_buu_chinh = [
    ("Thành phố Hồ Chí Minh", "700000"),
    ("Quận 1, TP.Hồ Chí Minh", "700001"),
    ("Quận 3, TP.Hồ Chí Minh", "700002"),
    ("Hà Nội", "100000"),
    ("Quận Hoàn Kiếm, Hà Nội", "100001"),
    ("Quận Ba Đình, Hà Nội", "100002"),
    ("Đà Nẵng", "550000"),
    ("Quận Hải Châu, Đà Nẵng", "551000"),
    ("Quận Thanh Khê, Đà Nẵng", "552000"),
    ("Hải Phòng", "180000"),
    ("Quận Hồng Bàng, Hải Phòng", "181000"),
    ("Quận Ngô Quyền, Hải Phòng", "182000"),
    ("Cần Thơ", "900000"),
    ("Ninh Kiều, Cần Thơ", "901000"),
    ("Cái Răng, Cần Thơ", "902000"),
    # V.v
]
def la_ma_buu_chinh_hop_li(diem_quan_trong, ma_buu_chinh):
    for diem_quan_trong, ma_buu_chinh in diem_quan_trong_va_ma_buu_chinh:
        if diem_quan_trong and ma_buu_chinh:
            return True
    return False
# Sử dụng hàm để kiểm tra mã bưu chính cho điểm quan trọng cụ thể
ket_qua = la_ma_buu_chinh_hop_li(diem_quan_trong_can_kiem_tra, ma_buu_chinh_can_kiem_tra)

print(ket_qua)