# coding=utf-8

'''
题目：将 第 0015 题中的 city.xls 文件中的内容写到 city.xml 文件中
思路：xml
'''

from xml.dom.minidom import Document

filename = 'static/city.txt'

with open(filename, 'r') as f:
    contents = f.read()

# contents = eval(contents)
print(contents)

comments = '''
<!--
        城市信息
-->
'''



def writeToXml(path, data):
    doc = Document()

    root = doc.createElement('root')

    doc.appendChild(root)

    student = doc.createElement('student')
    root.appendChild(student)

    student_text = doc.createTextNode(comments + contents + '\n')
    student.appendChild(student_text)

    with open(path, 'wb') as f:
        f.write(doc.toprettyxml(indent='\t', encoding='utf-8'))



if __name__ == '__main__':
    writeToXml('static/city.xml', contents)