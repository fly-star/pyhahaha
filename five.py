# coding=utf-8

'''
题目：任一个英文的纯文本文件，统计其中的单词出现的个数
思路：正则匹配
'''

import re

filepath = 'static/test.txt'

with open(filepath, 'r') as f:
    total = 0
    for line in f:
        each = re.split(r'[\s,\.\?!\’]+', line.strip())
        #过滤空元素
        each = list(filter(lambda x: x, each))
        print(each)
        eachLength = len(each)
        print(eachLength)
        total += eachLength
    print(total)