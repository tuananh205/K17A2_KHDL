def tinh_A(n,x):
    A=((x**2)+x+1)**n+((x**2)-x+1)**n
    print('S=',A)
    return 
n=float(input('nhập số n:'))
x=float(input('nhập số x:'))
tinh_A(n,x)
