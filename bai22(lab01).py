# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 19:54:05 2024

@author: TranThiTuyetMai
"""
a = float(input(" nhập số a: "))
b = float(input(" nhập số b: "))
if a == 0 and b == 0:
    print(" pt có vô số nghiệm")
elif a == 0 and b != 0:
    print(" pt vô nghiệm")
else:
    print(" pt có 1 nghiệm x=", -b/a)

