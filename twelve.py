# coding=utf-8

'''
题目：敏感词文本文件 filtered_words.txt，里面的内容 和 0011题一样，当用户输入敏感词语，则用 星号 * 替换，例如当用户输入「北京是个好城市」，则变成「**是个好城市」
思路：
'''

import pprint
import sys
import chardet


with open('static/filtered_words.txt', 'r') as f:
    words = [line.strip() for line in f]

pprint.pprint(words)


def inputGame():
    while True:
        contents = input('请输入>>')
        for word in words:
            if word in contents:
                lenth = len(word)
                contents = contents.replace(word, '*'*lenth)
        print(contents)

if __name__ == '__main__':
    inputGame()