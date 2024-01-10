import string
a=str(input('nhập chuỗi:'))
s_sub=str(input('nhập chuỗi con s_sub:'))
s_find=str(input('nhập chuỗi tìm s_find:'))
s_replace=str(input('nhập chuỗi thay thế s_replace:'))
print('chuỗi sau khi loại bỏ khoảng trắng ở đầu và cuối:',a.strip())
print('số lần s_sub xuất hiện trong chuỗi',a.count(s_sub))
print('chuỗi s sau khi tìm kiếm và thay thế:',a.replace(s_find,s_replace))