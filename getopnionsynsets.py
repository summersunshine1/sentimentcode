import codecs
from nltk.corpus import wordnet as wn
from nltk.probability import FreqDist
import os

def getopnion(file_path):
    file_object = codecs.open(file_path,'r','utf-8')
    featurearr = []
    try:
        all_text = file_object.read()
        arr = all_text.split()
    finally:
        file_object.close()
    return arr

def create_txt(file_path, content):
    if os.path.exists(file_path):
        os.remove(file_path)
    f=codecs.open(file_path,'w','utf-8')
    for x in content:
        f.write(x)
        f.write('\n')
    f.close()
    
def getopinionsynset():
    synsetdic= dict()
    arr = getopnion("F:/course/sentimentcode/feature/data/newopinion")
    fdist = FreqDist()
    for word in arr:
        synsets = wn.synsets(word, wn.ADJ)
        for synset in synsets:
            for lemma in synset.lemmas():
                fdist[lemma.name()]+=1
                for l in lemma.antonyms():
                    fdist[l.name()]+=1
    arr = fdist.most_common(30)
    commonadj = []
    for wordpair in arr:
        commonadj.append(wordpair[0])
    create_txt("F:/course/sentimentcode/feature/data/commonadj", commonadj)    
           
getopinionsynset()