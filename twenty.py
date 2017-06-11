# coding=utf-8

'''
题目：登陆中国联通网上营业厅 后选择「自助服务」 --> 「详单查询」，然后选择你要查询的时间段，点击「查询」按钮，查询结果页面的最下方，点击「导出」，就会生成类似于 2014年10月01日～2014年10月31日通话详单.xls 文件。写代码，对每月通话时间做个统计
思路：HTML解析
'''

import re
from bs4 import BeautifulSoup as bsp

with open(r'/home/flystar/下载/13588214965.html', 'rb') as f:
    html = f.read()

soup = bsp(html, 'lxml')

res = []
tdd = soup.find_all('tr', attrs={'class': 'content2'})
for tr in tdd:
    trs = tr.find_all('td', attrs={'class': 'talbecontent1'})
    try:
        res.append(trs[2].text)
    except:
        pass

patten1 = r'(\d+)秒'
patten2 = r'(\d+)分(\d+)秒'
patten3 = r'(\d+)时(\d+)分(\d+)秒'

times = []
for each in res:
    try:
        m = next(re.match(x, each) for x in [patten1,patten2, patten3] if re.match(x, each))
    except StopIteration:
        print('%s未成功匹配'%each)
    else:
        lists = m.groups()
        if len(lists) == 2:
            m, s = lists
            times.append(int(m)*60 + int(s))
        elif len(lists) == 3:
            h, m, s = lists
            times.append(int(h)*3600 + int(m)*60 + int(s))
        elif len(lists) == 1:
            times.append((int(lists[0])))

totalSeconds = sum(times)
h, s = divmod(totalSeconds, 3600)
m, s = divmod(s, 60)
print('5月通话总时长为: %s时%s分%s秒'%(h, m, s))

