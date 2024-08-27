# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 18:26:40 2024

@author: Admin
"""
thoi_gian = input("nhập thời gian (hh:mm:ss)")
gio, phut, giay = map(int, thoi_gian.split(":"))
tong_giay = gio *3600 + phut *60 + giay
print(" tong so giay la:", tong_giay)
