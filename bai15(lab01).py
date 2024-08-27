# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 18:22:18 2024

@author: TranThiTuyetMai
"""
a = int(input("nhập a là"))
b = int(input("nhập b là"))
A = ((a + b) / (pow(a,(1 / 3)) + pow(b,(1 / 3)))) - pow(a * b,(1 / 3))
B = (pow(a,(1 / 3)) - pow(b,(1 / 3))) ** 2
print("kết quả là", A / B)
