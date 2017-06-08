# coding=utf-8

'''
题目：你有一个目录，装了很多照片，把它们的尺寸变成都不大于 iPhone5 分辨率的大小
思路：使用glob和PIL
'''

import glob
from PIL import Image

formats = ['.jpg', '.png']
sizes = (640, 1136)
count = 1

for format in formats:
    imgs = glob.iglob(r'static/*%s'%format)
    for img in imgs:
        img_ = Image.open(img)
        img_.thumbnail(sizes)
        img_.save('static/thumbnail%s.jpg'%count)
        count += 1
