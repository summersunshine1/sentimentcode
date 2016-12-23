# -*- coding:utf-8 -*-
import os
import codecs
from collections import OrderedDict
def readfile(filepath):
    file_object = codecs.open(filepath,'r','utf-8')
    try:
        lines = file_object.readlines()
        newlines = []
        for line in lines:
            dic = OrderedDict()
            if '\n' in line:
                line = line.replace('\n', '')
                arr = line.split()
                for word in arr:
                    if word in dic:
                        dic[word] += 1
                    else:
                        dic[word] = 1    
            newlines.append(dic)
    finally:
        file_object.close()
    return newlines


def create_txt(file_path, content):
    if os.path.exists(file_path):
        os.remove(file_path)
    f=codecs.open(file_path,'w','utf-8')
    for x in content:
        f.write(x)
        f.write('\n')
    f.close()
    
lines = readfile('F:/course/sentimentcode/feature/data/newnoun')
newlines = []
for line in lines:
    newstr = ''
    for k,v in line.items():
        if v==1:
            newstr+=k
        else:
            newstr+=k
            newstr+='='
            newstr+=str(v)
        newstr+=','
    newlines.append(newstr)
create_txt('F:/course/sentimentcode/feature/data/newnoun.basket', newlines)
    
        