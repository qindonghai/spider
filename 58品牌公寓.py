#!/bin/env python 
#coding=utf-8
import urllib
import urllib2
import re
import string
from  bs4 import  BeautifulSoup
import csv
def zufang(url):
    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    headers = { 'User-Agent' : user_agent }
    req=urllib2.Request(url,headers=headers)
    res=urllib2.urlopen(req)
    page=res.read(res)
    soup=BeautifulSoup(page,'lxml')
    get_url=soup.find_all('a',{'onclick':"clickLog('from=fcpc_list_gy_qd_tupian')"})
    for n in range(len(get_url)):
        total_url='http://qd.58.com'+get_url[n]['href']
        user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        headers = { 'User-Agent' : user_agent }
        req=urllib2.Request(total_url,headers=headers)
        res=urllib2.urlopen(req)
        page=res.read(res)
        soup=BeautifulSoup(page,'lxml')
        get_price=soup.find_all('span',{'class':"price"})
        for i in range(len(get_price)):
            price=get_price[i].string
        get_title=soup.title.string.encode("utf8")
        get_longitude=re.findall('.*json4fe.lon.*',page)[0].split("'")[1].encode("utf8")
        get_latitude=re.findall('.*json4fe.lat.*',page)[0].split("'")[1].encode("utf8")
        print '*'*5+"Get the "+str(n)+"page"+'*'*5
        csv_file=open("addr.csv","a")
        csv_writer=csv.writer(csv_file,delimiter=',')
        csv_writer.writerow([get_title,get_title,get_longitude,get_latitude,total_url,price])
        csv_file.close() 


for i in range(100):
    url='http://qd.58.com/pinpaigongyu/pn/'+str(i)+'/?key=%E5%93%81%E7%89%8C%E5%85%AC%E5%AF%93&PGTID=0d3111f6-0007-a7b9-cc24-c184787319c6&ClickID=1'
    print '*'*10+'Reading the '+str(i)+' Page'+'*'*10
    zufang(url)
    

