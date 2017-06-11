# coding=utf-8

'''
题目：通常，登陆某个网站或者 APP，需要使用用户名和密码。密码是如何加密后存储起来的呢？请使用 Python 对密码加密
思路：盐值加算法加密
'''

import hashlib
import os
import hmac


def encryptPassword(password, salt=None):
    if not salt:
        salt = os.urandom(8)
    pwd = password.encode('utf-8')
    res = hmac.new(pwd, salt, hashlib.sha256).hexdigest()
    return res


pwd = 'secret key'
pwdAfter = encryptPassword(pwd)
print(pwdAfter)
