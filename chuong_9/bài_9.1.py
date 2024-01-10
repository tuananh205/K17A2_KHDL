def sign(x):
    if x>0:
        a=1
    elif x<0:
        a=-1
    else:
        a=0
    return a
x=float(input('nhập số:'))
print(sign(x))
