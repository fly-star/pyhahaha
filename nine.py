# coding=utf-8

'''
题目：一个HTML文件，找出里面的正文
思路：使用beautifulsoup4解析
'''
import pprint
from bs4 import BeautifulSoup as bsp
import requests

res = requests.get('http://www.baidu.com')

soup = bsp(res.content, 'lxml')

pprint.pprint(soup.body)

aLists = soup.find_all('a')

for a in aLists:
    print(a.string)

