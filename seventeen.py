# coding=utf-8

'''
题目：将 第 0014 题中的 student.xls 文件中的内容写到 student.xml 文件中
思路：xml
'''

from xml.dom.minidom import Document

filename = 'static/student.txt'

with open(filename, 'r') as f:
    contents = f.read()

# contents = eval(contents)
print(contents)

comments = '''
<!--
        学生信息表
        "id": [名字, 数学, 语文, 英文]
-->
'''



def writeToXml(path, data):
    doc = Document()

    root = doc.createElement('root')

    doc.appendChild(root)

    student = doc.createElement('student')
    root.appendChild(student)

    student_text = doc.createTextNode(comments + contents)
    student.appendChild(student_text)

    with open(path, 'wb') as f:
        f.write(doc.toprettyxml( encoding='utf-8'))



if __name__ == '__main__':
    writeToXml('static/student.xml', contents)