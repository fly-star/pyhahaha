# coding=utf-8

'''
题目：用 Python 写一个爬图片的程序，爬http://tieba.baidu.com/p/2166231880这个链接里的日本妹子图片
'''

import re
import os
from collections import deque
import requests
from bs4 import BeautifulSoup as bsp


#调度器
class Dispatcher(object):
    def __init__(self, start='http://tieba.baidu.com/p/2166231880'):
        self.url_ = URLManager(start)
        self.down_ = Downloader()
        self.parser_ = HTMLParser()
        self.img_ = ImgGener()
        self.done = True

    def getUrl(self):
        if self.url_.urls:
            return self.url_.urls.popleft()
        else:
            self.done = False

    def downUrl(self, url):
        return self.down_.down(url)

    def parserHtml(self, resp):
        imgs, as_ = self.parser_.parser(resp)
        diffs = set(as_).difference(set(self.url_.urls))
        self.url_.urls.extend(diffs)
        diffs2 = set(imgs).difference(set(self.url_.imgSrcs))
        self.url_.imgSrcs.extend(diffs2)

    def createImg(self, url):
        img = requests.get(url)
        self.img_.createImg(img.content)

    def run(self):
        while self.done:
            url = self.getUrl()
            print(url)
            resp = self.downUrl(url)
            if resp:
                self.parserHtml(resp)


        for imgUrl in self.url_.imgSrcs:
            self.createImg(imgUrl)
        print(self.img_.count)

#url管理器
class URLManager(object):
    def __init__(self, start):
        self.urls = deque()
        self.urls.append(start)
        self.imgSrcs = list()


#HTML下载器
class Downloader(object):
    def __init__(self):
        pass

    def down(self, url):
        try:
            resp = requests.get(url)
            return resp
        except:
            pass



#HTML解析器
class HTMLParser(object):
    def __init__(self):
        pass

    def parser(self, resp):
        soup = bsp(resp.content, 'lxml')
        imgs = soup.find_all('img', bdwater=re.compile('杉本有美吧'))
        as_ = soup.find_all('a')
        imgAddrs = [img['src'] for img in imgs]
        return imgAddrs, as_

#img处理器
class ImgGener(object):
    def __init__(self, dirname='static/scri'):
        self.dirname = dirname
        self.imgName = '杉本有美'
        self.count = 1

    def createImg(self, imgData):
        self.filename = os.path.join(self.dirname, self.imgName + str(self.count))
        with open(self.filename, 'wb') as f:
            try:
                f.write(imgData)
            except:
                print('{}写入失败'.format(self.filename))
                return
            else:
                self.count += 1

if __name__ == '__main__':
    mycri = Dispatcher()
    mycri.run()
