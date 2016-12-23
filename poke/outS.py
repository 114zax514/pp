#coding: utf-8
import urllib2
from bs4 import BeautifulSoup

html = urllib2.urlopen("http://pente.koro-pokemon.com/data/ranking-speed.shtml")
soup = BeautifulSoup(html)
th2 = soup(class_="th2")
#  print th2
#  print len(th2)
for i in range(0,len(th2)):
    print soup(class_="th2")[i].renderContents()

poke = soup("*zukan*")
for i in range(0,len(poke)):
    print soup("*zukan*")[i].renderContents()
