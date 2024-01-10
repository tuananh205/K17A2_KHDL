tuple_a=3,1,2,4
tuple_b=5,7,6,8
tuple_c=tuple_a+tuple_b
print('tuple_c:',tuple_c)
a=list(tuple_c)
a.sort()
tuple_d=tuple(a) 
print('tuple_d:',tuple_d)
print('tuple[3]=',tuple_d[3])
print('3 phần tử cuối cùng của tuple d',tuple_d[-3:])