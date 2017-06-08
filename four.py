# coding=utf-8

'''
题目：将 0001 题生成的 200 个激活码（或者优惠券）保存到 Redis 非关系型数据库中
思路：使用redis
'''

import random
import redis

def genActiveCodes(nums):
    res = []
    #ascii码,48等于数字0,90等于大写Z
    Strs = [chr(n) for n in range(48, 58)] + [chr(n) for n in range(65, 91)]

    for _ in range(nums):
        temp = ''.join([random.choice(Strs) for _ in range(15)])
        res.append(temp)

    return res

def saveToRedis(seq):
    conn = redis.Redis('localhost', 6379)
    for index, each in enumerate(seq):
        conn.set(index, each)
    return conn

if __name__ == '__main__':
    res = genActiveCodes(200)
    conn = saveToRedis(res)
    value = conn.get('14')
    print(value.decode('utf-8'))
