# coding=utf-8
'''
题目：将 0001 题生成的 200 个激活码（或者优惠券）保存到 MySQL 关系型数据库中
思路：使用pymysql
'''

import random
import pymysql

def genActiveCodes(nums):
    res = []
    #ascii码,48等于数字0,90等于大写Z
    Strs = [chr(n) for n in range(48, 58)] + [chr(n) for n in range(65, 91)]

    for _ in range(nums):
        temp = ''.join([random.choice(Strs) for _ in range(15)])
        res.append(temp)

    return res

#建立数据库连接
class WriteToDB(object):
    def __init__(self, host='localhost', user='root', passwd='ct', db='flystar_deve'):
        self.conn = pymysql.Connect(host=host,
                                    user=user,
                                    passwd=passwd,
                                    db=db,
                                    charset='utf8')
        self.cursor = self.conn.cursor()

    def createTable(self, tablename=None):
        sql = '''
drop table if exists `{0}`;
create table `{0}` (
    `id` int(4) not null auto_increment,
    `code` varchar(50),
    primary key (`id`),
    unique key (`code`)
) engine=InnoDB CHARSET=utf8;
'''.format(tablename)

        self.cursor.execute(sql)
        self.conn.commit()

    def insert(self, table='activeCodes', **kw):
        sql = "insert into {table} (`code`) values ('{code}')".format(table=table, code=kw.get('code'))
        self.cursor.execute(sql)
        self.conn.commit()
        print('成功插入', self.cursor.rowcount, '条数据')

    def update(self, table='activeCodes', **kw):
        sql = "update {table} set `code`='{code}' where `id`='{id}'".format(table=table, code=kw.get('code'), id=kw.get('id'))
        self.cursor.execute(sql)
        self.conn.commit()
        print('成功修改', self.cursor.rowcount, '条数据')

    def select(self, table='activeCodes', **kw):
        if kw.get('id'):
            sql = "select {code} from {table} where id='{id}'".format(table=table, code=kw.get('code'), id=kw.get('id'))
        else:
            sql = "select {code} from {table}".format(table=table, code=kw.get('code'))
        self.cursor.execute(sql)
        print('成功找到', self.cursor.rowcount, '条数据')
        return self.cursor.fetchall()

    def delete(self, table='activeCodes', **kw):
        if kw.get('id'):
            sql = "delete from {table} where id='{id}'".format(table=table, id=kw.get('id'))
        else:
            sql = "delete from {table}".format(table=table)
        self.cursor.execute(sql)
        self.conn.commit()
        print('成功删除', self.cursor.rowcount, '条数据')

myWrite = WriteToDB()
myWrite.createTable(tablename='activeCodes')

res = genActiveCodes(200)
for code in res:
    myWrite.insert(code=code)

myWrite.update(code=genActiveCodes(1)[0], id=43)

code = myWrite.select(code='code', id=78)

myWrite.delete(id=78)
print(code)