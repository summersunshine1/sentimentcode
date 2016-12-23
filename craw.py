# -*- coding:utf-8 -*-
import urllib.request
import os
import shutil
import re
import codecs
import json
from bs4 import BeautifulSoup
import _thread

import sys   
sys.setrecursionlimit(1000000)  

def get_url(pno):
    url = "https://www.amazon.com/Fujifilm-Instax-Mini-Instant-Pink/product-reviews/B009ZM9R4O/ref=cm_cr_getr_d_paging_btm_"+str(pno)
    url = url + "?ie=UTF8&reviewerType=avp_only_reviews&showViewpoints=1&sortBy=recent&pageNumber="
    url = url+str(pno)
    return url

def get_html_soup(url,code):#获取解编码后的HTML
    html = None
    try:
        headers = {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
        req = urllib.request.Request(url=url, headers=headers)
        html = urllib.request.urlopen(req).read().decode(encoding = code, errors='ignore')
    except Exception as e:
        print(e, "please check your network situation")
        return None
    soup = BeautifulSoup(str(html), "lxml")   
    return soup
    
def get_review_body(url):
    content_text = []

    soup = get_html_soup(url, 'utf-8')
    if soup == None:
        return None
    review_div = str(soup.find("div", attrs = {"id": "cm_cr-review_list"}))
    soup = BeautifulSoup(str(review_div), "lxml")
    # create_txt("F:/course/sentimentcode/feature/data/temp.txt", soup.prettify())
    # review_data = str(soup.find("span", attrs = {"datahook": "review-body"}))
    # soup = BeautifulSoup(str(review_data), "lxml")
    para_arr = soup.find_all("span", attrs = {"class": "a-size-base review-text"})
    lenth = len(para_arr)
    for i in range(0,lenth - 1):
        if len(para_arr[i].get_text().strip()) > 0:
            content_text.append(para_arr[i].get_text().strip())
            # print(para_arr[i].get_text().strip())
    for x in content_text:
        if x == "None":
            return None
    return content_text

def create_txt(path, content):   
    filepath=path
    # if os.path.exists(filepath):
        # return
    f=None
    try:
        f=codecs.open(filepath,'w','utf-8')
        for x in content:
            for y in x:
                f.write(y)
                f.write('\n')
        # f.write(content)
    except Exception as e:
        return None    
    finally:
        if not f==None:
            f.close()
            print("create succeed")


def scrape(start,end,i):
    # totalpsize=762
    rootdir="F:/course/sentimentcode/feature/data"
    print("start"+str(start)+" end"+ str(end))
    wholecontent = []
    for j in range(start,end):
        url = get_url(j+1)
        content = get_review_body(url)
        if content==None:
            print("content none")
            continue
        print(str(j)+'page end')
        wholecontent.append(content)
    path = rootdir+'/corpus'
    path = path+str(i)
    create_txt(path, wholecontent)
            
# scrape()            
import time
import threading
if __name__ == '__main__':
    threads = []
    j = 0
    for i in range(10):
        thread = threading.Thread(target=scrape, args=(j,j+76,i,))
        j=j+76
        thread.start()
        threads.append(thread)
    #join must behind start
    for i in range(10):
        threads[i].join()
    


    
    
    
    
    
    
    
    
    
    
    
    
    