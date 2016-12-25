import codecs
import os
from textblob import TextBlob

def getopnion(file_path):
    file_object = codecs.open(file_path,'r','utf-8')
    featurearr = []
    try:
        all_text = file_object.read()
        arr = all_text.split()
    finally:
        file_object.close()
    return arr
    
def getreview(file_path):
    file_object = codecs.open(file_path,'r','utf-8')
    featurearr = []
    try:
        lines = file_object.readlines()
    finally:
        file_object.close()
    return lines
  
def getpolarity():
    reviewdic = readJsontodic("F:/course/sentimentcode/feature/data/featuredic")
    polarityscore = dict()
    for word,indexandarr in reviewdic.items():
        if not word in polarityscore:
            polarityscore[word]=[]
            polarityscore[word].append([])
            polarityscore[word].append([])
            polarityscore[word].append([])
        for indexdic in indexandarr:
            for index,wordarr,in indexdic.items():
                score = 0
                for w in wordarr:
                    blob = TextBlob(w)
                    for sentence in blob.sentences:
                        score += sentence.sentiment.polarity
                if score < 0:
                    polarityscore[word][0].append(index)
                if score == 0:
                    polarityscore[word][1].append(index)
                if score > 0:
                    polarityscore[word][2].append(index)
    return polarityscore
    
import json 
def readJsontodic(filepath):
    file_object = codecs.open(filepath,'r','utf-8')
    dic = json.load(file_object)
    return dic
    
def writepolarity(file_path):
    polarityscore = getpolarity()
    reviewlines = getreview("F:/course/sentimentcode/feature/data/corpus")
    if os.path.exists(file_path):
        os.remove(file_path)
    f=codecs.open(file_path,'w','utf-8')
    for word,sentencesarr in polarityscore.items():
        f.write(word+':\n')
        f.write("postive:\n")
        for i in sentencesarr[2]:
            f.write(reviewlines[int(i)])
        f.write(word+':\n')
        f.write("negative:\n")
        for i in sentencesarr[0]:
            f.write(reviewlines[int(i)])
        f.write(word+':\n')
        f.write("neutral:\n")
        for i in sentencesarr[1]:
            f.write(reviewlines[int(i)])
        f.write('\n')
    f.close()
        
writepolarity("F:/course/sentimentcode/feature/data/reviewsummerization")        
    
        
    
    
    
