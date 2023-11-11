def kiem_tra_nam_nhuan(nam):
    if (nam % 4 == 0 and nam % 100 != 0) or (nam % 400 == 0):
        return f"{nam} là năm nhuận."
    else:
        return f"{nam} không phải là năm nhuận."

# Nhập năm vào
nam = int(input("Nhập năm cần kiểm tra: "))

# In kết quả
print(kiem_tra_nam_nhuan(nam))