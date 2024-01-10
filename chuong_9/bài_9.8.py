x=int(input('nhập số:'))
s=0
def kiem_tra_so_hoan_hao(x,s):   
 for i in range(1,x-1):
        if x%i==0:
            s+=i
 return s

kiem_tra_so_hoan_hao(x,s)
if x==1:
    print('1 là số hoàn hảo')
elif s==x:
    print(x,'là số hoàn hảo')
else:
    print(x,'là số không hoàn hảo')
    