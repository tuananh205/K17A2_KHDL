def BMI(can_nang,chieu_cao):
    BMI=can_nang/(chieu_cao*chieu_cao)
    print('chỉ số BMI:%.2f'%BMI)
    if BMI<18.5:
        print('đánh giá theo chỉ số:Gầy')
    elif BMI>=18.5 and BMI<25:
        print('đánh giá theo chỉ số:Bình Thường')
    else:
        print('đánh giá theo chỉ số:Thừa Cân')
    return 
a=float(input('nhập cân nặng(kg):'))
b=float(input('nhập chiều cao(m):'))
BMI(a,b)
