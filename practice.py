# coding=utf-8

import re

patten1 = r'(\d+)秒'
patten2 = r'(\d+)分(\d+)秒'
patten3 = r'(\d+)时(\d+)分(\d+)秒'


s = '10时8分9秒'
s1 = '9秒'

b = re.search(patten3, s1)
print(b)