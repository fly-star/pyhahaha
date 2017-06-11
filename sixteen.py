# coding=utf-8

'''
题目：纯文本文件 numbers.txt, 里面的内容（包括方括号）如下所示，请将上述内容写到 numbers.xls 文件中
思路：xlsxwriter
'''

import xlsxwriter
filename = 'static/numbers.txt'

with open(filename, 'r') as f:
    contents = f.read()

contents = eval(contents)


def writeToXls(path, data):
    wb = xlsxwriter.Workbook(path)
    sheet = wb.add_worksheet('numbers')
    for index, value in enumerate(data):
        sheet.write_row(index, 0, value)

    wb.close()


if __name__ == '__main__':
    writeToXls('static/numbers.xls', contents)