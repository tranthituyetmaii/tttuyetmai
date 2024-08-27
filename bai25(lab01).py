# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 22:04:37 2024

@author: TranThiTuyetMai
"""
chucai = input("nhập chữ cái bất kì")
if chucai.islower():
    chucai = chucai.upper()
elif chucai.isupper():
    chucai = chucai.lower()
else:
    print("đây không phải là chữ cái hợp lệ") 
print("hợp lê", chucai)
       
       
