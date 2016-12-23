import operator
from orangecontrib.associate.fpgrowth import *
import Orange
import codecs
import os

def create_txt(file_path, content):
    if os.path.exists(file_path):
        os.remove(file_path)
    f=codecs.open(file_path,'w','utf-8')
    for x in content:
        f.write(x)
        f.write('\n')
    f.close()

def write_feature(file_path, content):
    if os.path.exists(file_path):
        os.remove(file_path)
    f=codecs.open(file_path,'w','utf-8')
    for x in content:
        for y in x:
            f.write(y)
            f.write('\n')
    f.close()
    
def readfile(filepath):
    file_object = codecs.open(filepath,'r','utf-8')
    word = []
    flag = dict()
    try:
        newarr = []
        all_text = file_object.read()
        arr = all_text.split()
        for a in arr:
            if not a in flag:
                newarr.append(a)
                flag[a]=1
                
    finally:
        file_object.close()
    create_txt("F:/course/sentimentcode/feature/data/wordset",newarr)
    return newarr

def redundencyprune(res, frequency, threshold):
    freqdist = dict()
    reslen = len(res)
    for i in range(reslen):
        wordarr = res[i]
        l = len(wordarr)
        for j in range(l):
            dic = dict()
            dic[l]=frequency[i][j]
            word = wordarr[j]
            if not word in freqdist:
                freqdist[word] = []
            freqdist[word].append(dic)
    removewords = []
    for k,v in freqdist.items():
        if len(v)>1:
            sum = 0
            for d in v:
                for k1,v1 in d.items():
                    if not k1 == 1:
                        sum = sum-v1
                    else:
                        sum = sum+v1
            if sum < threshold:
                removewords.append(k)
                print(k)
    for word in removewords:
        arr = []
        arr.append(word)
        res.remove(arr)
    return res
                    
           
file_path = 'F:/course/sentimentcode/feature/data/newnoun.basket'  
data = Orange.data.Table(file_path)
noun_path = 'F:/course/sentimentcode/feature/data/newnoun'
arr = readfile(noun_path)
X, mapping = OneHot.encode(data, include_class=False)
itemsets = dict(frequent_itemsets(X, .01))
itemsets = sorted(itemsets.items(), key=lambda x:x[1])
res = []
frequency = []
for item in itemsets:
    temp = []
    tempf = []
    for i in item[0]:
        temp.append(arr[i])
        tempf.append(item[1])
    res.append(temp)
    frequency.append(tempf)

res = redundencyprune(res, frequency, 200)
write_feature("F:/course/sentimentcode/feature/data/features", res)
        
