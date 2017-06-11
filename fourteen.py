# coding=utf-8

'''
题目：纯文本文件 student.txt为学生信息, 里面的内容（包括花括号）如下所示
思路：xlsxwriter
'''

import xlsxwriter
filename = 'static/student.txt'

with open(filename, 'r') as f:
    contents = f.read()

contents = eval(contents)


def writeToXls(path, data):
    wb = xlsxwriter.Workbook(path)
    sheet = wb.add_worksheet('student')
    for index, (key, value) in enumerate(data.items()):
        sheet.write_row(index, 0, [key] + value)

    wb.close()


if __name__ == '__main__':
    writeToXls('static/student.xls', contents)