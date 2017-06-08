# coding=utf-8

'''
题目：将你的 QQ 头像（或者微博头像）右上角加上红色的数字，类似于微信未读信息数量那种提示效果。 类似于图中效果

思路：使用PIL库
'''

from PIL import Image, ImageDraw, ImageFont
import os


def addNumToImg(img='static/one.png'):
    img_ = Image.open(img, 'r')
    width, height = img_.size
    img_.thumbnail((128, 128))
    position = (width*(3/4), height*(1/4))
    fonts = ImageFont.truetype("/usr/share/fonts/truetype/UbuntuMono-R.ttf", 10)

    draw = ImageDraw.Draw(img_)
    fillColer = '#FF1E25'
    draw.text(position, '9', font=fonts, fill=fillColer)
    dir, base = os.path.split(img)
    img_.save(base, 'jpeg')
    img_.show()
    print('end')


if __name__ == '__main__':
    addNumToImg()

