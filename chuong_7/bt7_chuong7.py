# gồm các loại tiền: 500000, 200000, 100000, 50000
tien_muon_doi = 1375000
print('số tiền muốn đổi:',tien_muon_doi)
so_to_1 = tien_muon_doi//500000
print('số tờ 500000:',so_to_1)
tien_con_lai = tien_muon_doi%500000
so_to_2 = tien_con_lai//200000
print('số tờ 200000:',so_to_2)
tien_con_lai = tien_con_lai%200000
so_to_3 = tien_con_lai//100000
print('số tờ 100000:',so_to_3)
tien_con_lai = tien_con_lai%100000
so_to_4 = tien_con_lai//50000
print('số tờ 50000:',so_to_4)
tien_con_lai = tien_muon_doi%50000
print('số tiền còn lại:',tien_con_lai)