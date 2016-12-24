import codecs
from nltk.corpus import wordnet as wn
from nltk.probability import FreqDist

def getopnion(file_path):
    file_object = codecs.open(file_path,'r','utf-8')
    featurearr = []
    try:
        all_text = file_object.read()
        arr = all_text.split()
    finally:
        file_object.close()
    return arr
 
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
    print(fdist.most_common(30))
        
getopinionsynset()