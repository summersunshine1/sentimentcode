import os
import codecs
import nltk
import enchant
import re
wordlist = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
def getopnion(file_path):
    file_object = codecs.open(file_path,'r','utf-8')
    featurearr = []
    try:
        all_text = file_object.read()
        arr = all_text.split()
    finally:
        file_object.close()
    return arr
   
def create_txt1(file_path, content):
    if os.path.exists(file_path):
        os.remove(file_path)
    f=codecs.open(file_path,'w','utf-8')
    for x in content:
        f.write(x)
        f.write('\n')
    f.close()
    
def featureshandle():
    featurearr = getopnion("F:/course/sentimentcode/feature/data/opinion")
    newfeature = []
    d = enchant.Dict("en_US")
    for feature in featurearr:
        arr = []
        #handle with misspelled word
        if not d.check(feature):
            suggest = d.suggest(feature)
            if len(suggest)==0:
                feature = ""
            else:
                feature = suggest[0]
        if feature=="":
            continue
        #remove single-word word
        if feature in wordlist:
            continue
        #remove word containing digit
        if re.search('\d', feature):
            continue
        newfeature.append(feature)
        # arr.append(feature)
        # taglist = nltk.pos_tag(arr)
        # for tag in taglist:
            # if tag[1]=='JJ':
                # newfeature.append(tag[0])
            # else:
                # print(tag)
    create_txt1("F:/course/sentimentcode/feature/data/newopinion", newfeature)
    
featureshandle()