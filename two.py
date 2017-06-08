# coding=utf-8

"""
题目：做为 Apple Store App 独立开发者，你要搞限时促销，为你的应用生成激活码（或者优惠券），使用 Python 如何生成 200 个激活码（或者优惠券）？
思路：使用random模块
"""

import random
import pprint


def genActiveCodes(nums):
    res = []
    #ascii码,48等于数字0,90等于大写Z
    Strs = [chr(n) for n in range(48, 58)] + [chr(n) for n in range(65, 91)]
    print(Strs)

    for _ in range(nums):
        temp = ''.join([random.choice(Strs) for _ in range(15)])
        res.append(temp)

    return res

res = genActiveCodes(200)
pprint.pprint(res)