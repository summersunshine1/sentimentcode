# -*- coding:utf-8 -*-
from nltk.tokenize import StanfordTokenizer
import nltk
from nltk import *
import codecs
from nltk.stem import WordNetLemmatizer

def readfile(filepath):
    file_object = codecs.open(filepath,'r','utf-8')
    try:
        all_text = file_object.read()
    finally:
        file_object.close()
    return all_text

linenoun = []

def traverse(t):
    try:
        t.label()
    except AttributeError:
        return linenoun
    else:
        if t.label()=='NP':
            onenp =[]
            arr = t.leaves()
            for a in arr:
                temp = a.split('/')
                onenp.append(temp[0])
            linenoun.append(onenp)
            for child in t:
                 traverse(child)
        else:
            for child in t:
                traverse(child)
 
def chunk(filepath):
    all_text = readfile(filepath)
    tokenizer = StanfordTokenizer()
    wordnet_lemmatizer = WordNetLemmatizer()
    arr = tokenizer.tokenize(all_text)
    grammar = "NP: {<JJ>*<NN>+}"
    cp = nltk.RegexpParser(grammar)
    res = []
    for line in arr:
        ar = line.split()
        newarr = []
        for i in ar:
            a = wordnet_lemmatizer.lemmatize(i)
            newarr.append(a)
        list = nltk.pos_tag(newarr)
        if len(list)==0:
            continue
        result = cp.parse(list)
        if len(result)==0:
            continue
        res.append(str(result))
    return res
    
def getsymbol(file_path):
    file_object = codecs.open(file_path,'r','utf-8')
    try:
        alltext = file_object.read()
        symbols = alltext.split()
    finally:
        file_object.close()
    return symbols
    
def create_txt(file_path, content):
    if os.path.exists(file_path):
        os.remove(file_path)
    f=codecs.open(file_path,'w','utf-8')
    for x in content:
        for y in x:
            for z in y:
                f.write(z)
                f.write(' ')
            f.write('\n')
    f.close()
    
    
def write_lines(file_path, lines):
    if os.path.exists(file_path):
        os.remove(file_path)
    f=codecs.open(file_path,'w','utf-8')
    for line in lines:
        f.write(line)
        f.write('\n')
    f.close()

def isspace(line):
    l = len(line)
    re = ''
    for i in range(l):
        re+=' '
    if re==line:
        return True
    return False
        
    
res = chunk("F:/course/sentimentcode/feature/data/corpuswithoutstop")
nounarr = []
for r in res: 
    tree=Tree.fromstring(r)
    traverse(tree)
    if len(linenoun) == 0:
        continue
    nounarr.append(linenoun)
    linenoun = []#linenoun.clear() clear memory data   
symbols = getsymbol('F:/course/sentimentcode/feature/symbol.txt') 

nounpath = 'F:/course/sentimentcode/feature/data/noun'
create_txt(nounpath, nounarr)
file_object = codecs.open(nounpath,'r','utf-8')
newlines = []
try:
    lines = file_object.readlines()
    for line in lines:
        line = line.replace('\n','')
        for symbol in symbols: 
            if symbol in line:
                line = line.replace(symbol,' ')
                if len(line) == 0:
                    break
        if not len(line) == 0 and not isspace(line):
            newlines.append(line)    
finally:
    file_object.close()
newnounpath = 'F:/course/sentimentcode/feature/data/newnoun' 
write_lines(newnounpath,newlines)
    



    

        
        
        
