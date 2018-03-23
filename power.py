#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# n次方 x^n
def power(x, n = 2):
	if not isinstance(x, (int, float)):
		raise TypeError('bad operand type')
	if not isinstance(n, (int)):
		raise TypeError('bad operand type')
	if n == 0:
		return 1
	else:
		i = 1
		powerVal = 1
		while i <= n:
			powerVal = powerVal*x
			i +=1
		return powerVal


print('power(2, 0) =', power(2, 0))
print('power(2, 1) =', power(2, 1))
print('power(2, 3) =', power(2, 3))
print('power(2) =', power(2))
