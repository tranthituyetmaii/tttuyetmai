# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 19:10:52 2024

@author: TranThiTuyetMai
"""
a = int(input("nhập số nguyên a"))
b = int(input("nhập số nguyên b"))
c = int(input("nhập số nguyên c"))
d = int(input("nhập số nguyên d"))
minvalue = a
if b < minvalue:
    minvalue = b
if c < minvalue:
    minvalue = c
if d < minvalue:
    minvalue = d
print("kết quả nhỏ nhất", minvalue)
