# -*- coding:utf-8 -*-
import os
import codecs
import shutil
def create_txt(file_path, content):
    if os.path.exists(file_path):
        os.remove(file_path)
    f=codecs.open(file_path,'w','utf-8')
    for x in content:
        for y in x:
            f.write(y)
    f.close()

def combinefile():
    rootdir = "F:/course/sentimentcode/feature/data"
    dir = os.walk(rootdir)    
    finalpath="F:/course/sentimentcode/feature/data/corpus"
    content = []
    for parent,dirnames,filenames in dir:    #三个参数：分别返回1.父目录 2.所有文件夹名字（不含路径） 3.所有文件名字
        for filename in filenames:#输出文件信息
            path_name=os.path.join(parent,filename)
            file_object = codecs.open(path_name,'r','utf-8')
            try:
                lines = file_object.readlines()
                content.append(lines)
            finally:
                file_object.close()        
    create_txt(finalpath, content)
    # shutil.rmtree(rootdir)
combinefile()