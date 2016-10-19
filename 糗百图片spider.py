#!/bin/env python
#encoding:utf-8
import urllib
import urllib2
import re
import string
def get(st,ed,url):
    j=0
    for i in range(st,ed+1):
        user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        headers = { 'User-Agent' : user_agent }  
        req = urllib2.Request(url+str(i)+".html", headers = headers)
        myResponse = urllib2.urlopen(req) 
        myPage = myResponse.read() 
        unPage = myPage.decode("gb2312")
        enPage=unPage.encode("utf-8")
        #正则匹配的URL成列表
        myItems = re.findall('src="http://ww.*?"',enPage)
        #print myItems[0]       
        print "-"*20+"爬取第"+str(i)+"个页面"+"-"*20
        print "-"*20+"本页面共有"+str(len(myItems))+"个图片"+"-"*20
        for items in myItems:
             j+=1
             print "*"*20+"正在抓取第"+str(j)+"个图片"+"*"*20
             items=items.replace('"','').replace('src=','')
             lst=items.split('.')
            #print items
             
             name=str(j)+'.'+lst[3]
#            url_rest=lst[0]
             f=open(name,'w+')
             m=urllib2.urlopen(items).read()
             f.write(m)
             f.close()   
        #info=dict(zip(lst,Lst))

print u"""  
---------------------------------------  
   程序：图片爬虫  
   版本：1.0 
   作者：Q  
   日期：2016-09-28 
   语言：Python 2.6  
---------------------------------------  
"""  

st_page=int(raw_input("输入要下载的开始页面:\n"))
end_page=int(raw_input("输入要下载的结束页面:\n"))
url="http://www.qiubaichengren.com/"
get(st_page,end_page,url)

