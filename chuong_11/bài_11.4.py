a=[]
while True:
    b=int(input('nhập giá trị:'))
    a.append(b)
    c=int(input('tiếp tục nhập giá trị?  1:có   0:không'))
    if c==1:
        continue
    if c==0:
        break
x=int(input('nhập gía trị cần tìm x:'))
print("list:",a)
print('tổng các giá trị trong list',sum(a))
print(x,'xuất hiện',a.count(x),'lần trong list')
d=[]
for i in a:
    if i>x:
       d.append(i)
print('các số lớn hơn',x,'trong list:',d)
        