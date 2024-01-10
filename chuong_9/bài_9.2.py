def tinh_can(nam):
    a=nam%10
    if a==0:
     can="canh"
    if a==1:
     can="tân"
    if a==2:
     can="nhâm"
    if a==3:
     can="quý"
    if a==4:
     can="giáp"
    if a==5:
     can="ất"
    if a==6:
     can="bính"
    if a==7:
     can="đinh"
    if a==8:
     can="mậu"
    if a==9:
     can="kỷ"
    return can
def tinh_chi(nam):
    b=nam%12
    if b==0:
     chi="thân"
    if b==1:
     chi="dậu"
    if b==2:
     chi="tuất"
    if b==3:
     chi="hợi"
    if b==4:
     chi="tý"
    if b==5:
     chi="sửu"
    if b==6:
     chi="dần"
    if b==7:
     chi="mão"
    if b==8:
     chi="thìn"
    if b==9:
     chi="tỵ"
    if b==10:
     chi="ngọ"
    if b==11:
     chi="mùi"
    return chi
nam=int(input("nhập năm:"))
print('năm',nam,'lịch âm là năm',tinh_can(nam),tinh_chi(nam))

