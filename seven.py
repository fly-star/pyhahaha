# coding=utf-8

'''
题目：你有一个目录，放了你一个月的日记，都是 txt，为了避免分词的问题，假设内容都是英文，请统计出你认为每篇日记最重要的词
思路：文件匹配加正则匹配加collections.Counter计数
'''

import glob
import re
from collections import Counter


def totalImportantWord(word, dirname='static'):
    counter = Counter()
    for file in glob.iglob('%s/*.txt'%dirname):
        with open(file, 'r') as f:
            for line in f:
                each = re.split(r'[\s,\.\?!\’]+', line.strip())
                counter += Counter(each)
    return counter.get(word)


nums = totalImportantWord('Issues')
print(nums)
