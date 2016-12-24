import os
import codecs
import nltk

def getfeature(file_path):
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
    featurearr = getfeature("F:/course/sentimentcode/feature/data/features")
    newfeature = []
    for feature in featurearr:
        arr = []
        arr.append(feature)
        taglist = nltk.pos_tag(arr)
        print(taglist)
        for tag in taglist:
            if tag[1]=='NN':
                newfeature.append(tag[0])
    create_txt1("F:/course/sentimentcode/feature/data/newfeatures", newfeature)
    
featureshandle()