# -*- coding:utf-8 -*-
import os
import codecs
from nltk.tokenize import StanfordTokenizer
def readfile(filepath):
    file_object = codecs.open(filepath,'r','utf-8')
    try:
        lines = file_object.readlines()
    finally:
        file_object.close()
    return lines

def getstoparr():
    file_object = codecs.open('F:/course/sentimentcode/feature/stopwords.txt','r','utf-8')
    arr = []
    try:
        all_the_text = file_object.read()
        arr = all_the_text.split()
    finally:
        file_object.close()
    return arr
    
def remove_stop():
    lines = readfile('F:/course/sentimentcode/feature/data/corpus')
    stopwords = getstoparr()
    content = []
    for line in lines:
        arr = line.split()
        newline=[]
        for word in arr:
            if word.lower() in stopwords:
                continue
            if 'www' in word.lower():
                continue
            newline.append(word.lower())
        content.append(newline)
    create_txt("F:/course/sentimentcode/feature/data/corpuswithoutstop",content)
        
def create_txt(file_path, content):
    if os.path.exists(file_path):
        os.remove(file_path)
    f=codecs.open(file_path,'w','utf-8')
    for x in content:
        for y in x:
            f.write(y)
            f.write(' ')
        f.write('\n')
    f.close()    
            
def getNP(filepath):
    all_the_text = readfile(filepath)
    tokenizer = StanfordTokenizer()
    arr = tokenizer.tokenize(all_the_text)
    
remove_stop()
    
    
