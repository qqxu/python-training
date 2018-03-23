#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 匹配txt文件中的关键字
dirction = open('keyWords.txt', 'r')

line = dirction.readlines()

arr = []
for ele in line:
	ele= ele.rstrip('\n')  # 移除换行符
	arr.append(ele)

your_word = input('please input any word:')
print(your_word in arr)

if (your_word in arr):
	print('Freedom')
else:
	print('Human Rights')	
		


dirction.close()