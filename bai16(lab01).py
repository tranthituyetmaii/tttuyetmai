# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 23:09:01 2024

@author: TranThiTuyetMai
"""

thoi_gian = input("Nhập thời gian (hh(h)mm(p)ss(s)): ")
so_thoi_gian = ""
for i in thoi_gian:
    if i.isalpha():
        so_thoi_gian += ":"
    else:
        so_thoi_gian += i
thoi_gian_dung = so_thoi_gian[:-1]
hh, pp, ss = map(int, thoi_gian_dung.split(":"))
so_giay = hh * 3600 + pp * 60 + ss
print(so_giay)