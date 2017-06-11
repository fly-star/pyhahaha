# coding=utf-8

'''
题目：使用 Python 生成类似于下图中的字母验证码图片 static/codes.jpg
思路：PIL库
'''
import random
from PIL import Image, ImageDraw, ImageFont, ImageFilter

#创建一张新图片
sizes = (60*4, 60)
colors = (255, 255, 255)
img = Image.new('RGB', sizes, colors)

#创建draw对象
draw = ImageDraw.Draw(img)

#创建字体对象
fonts = ImageFont.truetype('/usr/share/fonts/X11/Type1/a010013l.pfb', 36)

#生成随机字符
def genUpper():
    return chr(random.randint(65, 90))

#生成随机颜色,用于填充新图片背景
def genPixelColor():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))

#生成随机颜色，用于填充字符
def genChrColor():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))

#填充图片每个像素点
for h in range(sizes[1]):
    for w in range(sizes[0]):
        draw.point((w, h), genPixelColor())

#填充字符
for x, y in zip(range(30, 241, 60), [10]*4):

    draw.text((x, y), text=genUpper(), font=fonts, fill=genChrColor())

#模糊特效
img = img.filter(ImageFilter.BLUR)

#保存图片
img.save('static/code.jpg')