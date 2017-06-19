# coding=utf-8
'''
题目：逆转字符串——输入一个字符串，将其逆转并输出
'''

import random
import profile
import timeit


def reverseStr1(str):
	return str[::-1]

def reverseStr2(str):
	return ''.join(reversed(str))

chr_base = [chr(x) for x in range(65, 90)]
base = [random.choice(chr_base) for _ in range(100000000)]
str_ = ''.join(base)

print(timeit.timeit("reverseStr1('str_')", 'from __main__ import reverseStr1'))

print(timeit.timeit("reverseStr2('str_')", 'from __main__ import reverseStr2'))


