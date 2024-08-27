# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 19:10:41 2024

@author: TranThiTuyetMai
"""
soxe = int(input("nhập biển số xe của bạn:"))
chu_so_hang_nghin = soxe // 1000
chu_so_hang_tram = (soxe % 1000) // 100
chu_so_hang_chuc = ((soxe % 1000) % 100) // 10
chu_so_chu_don_vi = soxe % 10
tong_cac_chu_so = chu_so_hang_nghin + chu_so_hang_tram + chu_so_chu_don_vi + chu_so_chu_don_vi
a = tong_cac_chu_so // 10
b = tong_cac_chu_so % 10
sonut = a + b
c = sonut // 10
d= sonut % 10
print("số nút của bạn là:", c + d)

