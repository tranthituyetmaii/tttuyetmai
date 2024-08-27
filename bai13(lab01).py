# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 22:33:37 2024

@author: TranThiTuyetMai
"""
day = int(input("Nhập ngày: "))
month = int(input("Nhập tháng: "))
year = int(input("Nhập năm: "))
format_a = f"{day}/{month}/{year}"
format_b = f"{day}/{month}/{str(year)[2:]}"
format_c = f"{year}/{month}/{day}"
print("Định dạng a:", format_a)
print("Định dạng b:", format_b)
print("Định dạng c:", format_c)
input_a = input("Nhập theo định dạng Ngày/Tháng/Năm: ")
input_b = input("Nhập theo định dạng Ngày/Tháng/2 số cuối của Năm: ")
input_c = input("Nhập theo định dạng Năm/Tháng/Ngày: ")
day_a, month_a, year_a = map(int, input_a.split('/'))
day_b, month_b, year_b = map(int, input_b.split('/'))
year_b += 1900 if year_b > 50 else 2000
year_c, month_c, day_c = map(int, input_c.split('/'))
print("Kết quả từ định dạng a:", day_a, month_a, year_a)
print("Kết quả từ định dạng b:", day_b, month_b, year_b)
print("Kết quả từ định dạng c:", day_c, month_c, year_c)


