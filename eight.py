# coding=utf-8

'''
题目：你有一个目录，放了你一个月的日记，都是 txt，为了避免分词的问题，假设内容都是英文，请统计出你认为每篇日记最重要的词
思路：遍历文件，映射存储
'''

import os
import glob
import pprint
from collections import defaultdict

lanTypes = {
    'py': {
        'comment': '#'
    },
    'js': {
        'comment': '//'
    }
}


def totalCodes(dir):
    res = dict()
    for lan in lanTypes:
        res[lan] = defaultdict(int)
        files = glob.iglob('%s/*.%s'%(dir, lan))
        for file in files:
            with open(file, 'r') as f:
                for line in f:
                    if line.startswith(lanTypes[lan]['comment']):
                        res[lan]['comments'] += 1
                    elif line == '\n':
                        res[lan]['spaces'] += 1
                    else:
                        res[lan]['codes'] += 1
    return res


dirname = os.path.dirname(os.path.abspath(__file__))

res = totalCodes(dirname)

pprint.pprint(res)