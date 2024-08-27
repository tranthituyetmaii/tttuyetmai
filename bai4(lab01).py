# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 18:21:37 2024

@author: TranThiTuyetMai
"""
n = int(input(" nhập hai số nguyên dương có 2 chữ số"))
chu_so_hang_chuc = n // 10
chu_so_hang_don_vi = n % 10
tong_cac_chu_so = chu_so_hang_chuc + chu_so_hang_don_vi  
if 10 <= n <= 99:
  print("tong cac chu so cua n", tong_cac_chu_so) 

