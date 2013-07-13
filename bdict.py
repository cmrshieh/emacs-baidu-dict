#! /usr/bin/env python
# -*- coding: UTF-8 –*-

import urllib.request
from bs4 import BeautifulSoup
import sys

#COLUMN = "\033[30;47m" 
#TYPE = "\033[34;40m"
#CONTENT = "\033[37;40m"
#WARN = "\033[31;40m"

def main(words):
    url = 'http://dict.baidu.com/s?wd='
    if len(words) <=0:
        print ("没有选中关键词.")
    else:
        url = url +words[0]
        for word in words[1:]:
            url = url + '+' + word
        response = urllib.request.urlopen(url)
        html = response.read()
        soup = BeautifulSoup(html,"lxml")
        if( soup.find("div","noresult-tip") ):
            print("词典中没有与您搜索的关键词匹配的内容.")
            return 0
        
        print("简明释义")
        SimpleMeans = soup.find(id="en-simple-means")
        if SimpleMeans:
            mlist = SimpleMeans.find_all('p')
            for m in mlist:
                if(m.strong):
                    print(m.strong.string,m.span.string)
        else:
            print("没有相关解释")
            
        print("网络释义")
        NetMeans = soup.find(id="en-net-means")
        if NetMeans:
            mlist = NetMeans.find_all('p')
            for m in mlist:
                print(m.string)
        else:
            print("没有相关解释")

if __name__ == "__main__":
    main(sys.argv[1:])

