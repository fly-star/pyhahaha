# coding=utf-8

'''
题目： iPhone 6、iPhone 6 Plus 早已上市开卖。请查看你写得 第 0005 题的代码是否可以复用
思路：使用glob和PIL
'''

import glob
from PIL import Image

formats = ['.jpg', '.png']
sizes = (640, 1136)
sizes6 = (1334, 750)
count = 1

for format in formats:
    imgs = glob.iglob(r'static/*%s'%format)
    for img in imgs:
        img_ = Image.open(img)
        img_.thumbnail(sizes6)
        img_.save('static/thumbnail%s.jpg'%count)
        count += 1