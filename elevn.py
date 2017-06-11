# coding=utf-8

'''
题目：敏感词文本文件 filtered_words.txt，里面的内容为以下内容，当用户输入敏感词语时，则打印出 Freedom，否则打印出 Human Rights
思路：
'''

import pprint
import sys


with open('static/filtered_words.txt', 'r') as f:
    words = [line.strip() for line in f]

pprint.pprint(words)


def inputGame():
    while True:
        contents = input('请输入>>')
        if contents in words:
            print('Freedom')
        else:
            print('Human Rights')

if __name__ == '__main__':
    inputGame()