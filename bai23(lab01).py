# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 21:44:16 2024

@author: TranThiTuyetMai
"""
import math
a = float(input("Nhập số a: "))
b = float(input("Nhập số b: "))
c = float(input("Nhập số b: "))
denta = b * b - 4 * a * c
if a == 0: 
    print("phương trình có nghiệm duy nhất x=", -b/c)
elif a != 0 and denta < 0:
    print("phương trình vô nghiệm")
elif a != 0 and denta == 0:
    print("phương trình có nghiệm kép x1=x2 = ", -b/(2*a))
elif a != 0 and b*b - (4*a*c) > 0:
    print("phương trình có 2 nghiệm pb x1 = ", (-b + math.sqrt(denta))/(2 * a))
    print("phương trình có 2 nghiệm pb x2 = ", (-b - math.sqrt(denta))/(2 * a))
