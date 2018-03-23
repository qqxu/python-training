#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 一元二次方程求解 ax^2 + bx + c = 0
def quadratic(a, b, c):
	if not isinstance(a, (int, float)):
		raise TypeError('bad operand type')
	if not isinstance(b, (int, float)):
		raise TypeError('bad operand type')
	if not isinstance(c, (int, float)):
		raise TypeError('bad operand type')
	if a == 0:
		return -(c/b)
	else:
		import math
		x1 = (-b+math.sqrt(b*b - 4*a*c))/(2*a)
		x2 = (-b-math.sqrt(b*b - 4*a*c))/(2*a)
		return x1, x2

print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))
print('quadratic(0, 3, -4) =', quadratic(0, 3, -4))
