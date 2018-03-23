#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 测试身高体重BMI指数

# test BMI 
height = input('please input your height 0.00 :')
weight = input('please input youre weight 00.00 :')
bmi = float(weight)/(float(height)*float(height))
print('your bmi is: %s' % bmi)
if bmi < 18.5:
	print('低于18.5：过轻')
elif 18.5 <= bmi < 25:
	print('18.5-25：正常')
elif 25 <= bmi < 28:
	print('25-28：过重')
elif 28 <= bmi < 32:
	print('28-32：肥胖')
else:
	print('高于32：严重肥胖')