x=float(input('nhập số:'))
def kiem_tra_so_nguyen_to(x):
    if x<2:
        print(x,'không phải số nguyên tố')
    else:
        for i in range(2,int(x**0.5)+1):
               if x%i==0:
                     print(x,'không phải số nguyên tố')
                     break   
        else:
                   print(x,'là số nguyên tố')
    return 

kiem_tra_so_nguyen_to(x)
