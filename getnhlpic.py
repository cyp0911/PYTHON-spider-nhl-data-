#!/usr/bin/python
import re
import urllib


def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

def getImg(html,array):
    reg = r'\/><img src="(.*?photo.*?\.png)"'
    imgre = re.compile(reg)
    imglist = re.findall(imgre,html)
    x = 0
    for imgurl in imglist:
	token = array[x];
	urllib.urlretrieve(imgurl,'nhlstar/%s.png' % token)
	x+=1
    return imglist

def getName(html):
    reg1 = r'">([A-Z][a-z]{3,8})</span><span'
    namefind = re.compile(reg1)
    namelist = re.findall(reg1,html)
    x = 0
    return namelist
	
    


html = getHtml("http://www.nhl.com/stats/?navid=nav-sts-main#")
namelist1 = getName(html)
print namelist1;
print getImg(html,namelist1)
