from nltk.tokenize import StanfordTokenizer
import nltk
from nltk import *
import codecs
from nltk.stem import WordNetLemmatizer

def readreview(file_path):
    file_object = codecs.open(file_path,'r','utf-8')
    reviewarr = []
    wordnet_lemmatizer = WordNetLemmatizer()
    symbols = getsymbol('F:/course/sentimentcode/feature/symbol.txt')
    try:
        lines = file_object.readlines()
        for line in lines:
            line = line.replace('\n','')
            for s in symbols:
                if s in line:
                    line = line.replace(s,' ')
            ar = line.split()
            newarr = []
            for i in ar:
                a = wordnet_lemmatizer.lemmatize(i)
                newarr.append(a)
            reviewarr.append(newarr)
    finally:
        file_object.close()
    return reviewarr
 
def getnounandadj(file_path):
    reviewarr = readreview(file_path)
    nountag = "NN"
    adjtag = "JJ"
    noun=[]
    adj=[]
    arrwithna = []
    index = []
    initindex = 0
    for arr in reviewarr:
        newarr = []
        taglist = nltk.pos_tag(arr)
        l = len(taglist)
        tempnoun = set()
        tempadj = set()
        for i in range(l):
            if taglist[i][1] == nountag:
                tempnoun.add(taglist[i][0])
                newarr.append(taglist[i][0])
            if taglist[i][1] == adjtag:
                tempadj.add(taglist[i][0])
                newarr.append(taglist[i][0])
        if not len(tempnoun)==0:
            noun.append(list(tempnoun))
            adj.append(list(tempadj))
            arrwithna.append(newarr)
            index.append(initindex)
        initindex+=1
    return noun,adj,arrwithna,index
    
def create_txt(file_path, noun, adj):
    if os.path.exists(file_path):
        os.remove(file_path)
    f=codecs.open(file_path,'w','utf-8')
    lennoun = len(noun)
    for i in range(lennoun):
        l = len(noun[i])
        for j in range(l):
            f.write(noun[i][j])
            f.write(" ")
        l = len(adj[i])
        if l==0:
            f.write('\n')
            continue
        f.write(": ")
        for j in range(l):
            f.write(adj[i][j])
            f.write(" ")
        f.write('\n')
    f.close()

def getsymbol(file_path):
    file_object = codecs.open(file_path,'r','utf-8')
    try:
        alltext = file_object.read()
        symbols = alltext.split()
    finally:
        file_object.close()
    return symbols

def create_txt1(file_path, content):
    if os.path.exists(file_path):
        os.remove(file_path)
    f=codecs.open(file_path,'w','utf-8')
    for x in content:
        f.write(x)
        f.write('\n')
    f.close()

import json    
def writedictojson(file_path, dic):
    json.dump(dic, codecs.open(file_path,'w','utf-8'))

def getfeature(file_path):
    file_object = codecs.open(file_path,'r','utf-8')
    featurearr = []
    try:
        all_text = file_object.read()
        arr = all_text.split()
    finally:
        file_object.close()
    return arr
    
def extractopinion():
    (noun, adj,arrwithna,index) = getnounandadj("F:/course/sentimentcode/feature/data/corpuswithoutstop")#handle file make it leave only noun and adj
    create_txt("F:/course/sentimentcode/feature/data/nounadj",noun,adj)
    featurearr = getfeature("F:/course/sentimentcode/feature/data/newfeatures")
    
    l = len(noun)
    feature = dict()
    opinion = set()
    reviewstr = []
    
    for arr in arrwithna:
        str = ""
        for word in arr:
            str += word
            str += " "
        reviewstr.append(str)
    create_txt1("F:/course/sentimentcode/feature/data/reviewwithadjandnoun", reviewstr)
    for i in range(l):
        nounlen = len(noun[i])
        if nounlen == 1:#just one feature in a review,let all the adj in the review as opinions
            w = noun[i][0]
            effadj = set()
            dic = dict()
            if not w in featurearr:
                continue
            for a in adj[i]:
                opinion.add(a)
                effadj.add(a)
            if not w in feature:
                feature[w]=[]
            dic[index[i]] = list(effadj)
            feature[w].append(dic)
            continue
        for w in noun[i]:#many features in a review,every feature get its adj near it
            if not w in featurearr:
                continue
            if not w in feature:
                feature[w]=[]
            dic = dict()
            effadj = set()
            arr = reviewstr[i].split()
            indices = [j for j, s in enumerate(arr) if w in s]
            for j in indices:
                temp = j-1
                find = False
                while temp >= 0:
                    if arr[temp] in effadj:
                        break
                    if arr[temp] in noun[i]:#in other noun range
                        break
                    if arr[temp] in adj[i]:
                        effadj.add(arr[temp])
                        opinion.add(arr[temp])
                        find = True
                        break
                    temp-=1
                if find:
                    continue
                temp = j+1
                while temp<len(indices):
                    if arr[temp] in effadj:
                        break
                    if arr[temp] in noun[i]:
                        break
                    if arr[temp] in adj[i]:
                        effadj.add(arr[temp])
                        opinion.add(arr[temp])
                        break
                    temp += 1
                # reex = '((?:\w*\W*){,3})'
                # reex += '('
                # reex += w
                # reex += ')'
                # reex += '\W*((?:\w*\W*){,3})'
                # m = re.search(reex, reviewstr[i])#find effective opinions
                # if m:
                    # l = [ x.strip().split() for x in m.groups()]
                    # left, right = l[0], l[2]
                    
                    # for word in l[0]:
                        # if word in adj[i]:
                            # effadj.add(word)
                            # opinion.add(word)
                    # for word in l[2]:
                        # if word in adj[i]:
                            # effadj.add(word)
                            # opinion.add(word)
            dic[index[i]] = list(effadj)
            feature[w].append(dic)
    create_txt1("F:/course/sentimentcode/feature/data/opinion", opinion)
    writedictojson("F:/course/sentimentcode/feature/data/featuredic", feature) 
    
# featureshandle()
feature = extractopinion()
    
        
        
            
            
        
        
    
    

    

    