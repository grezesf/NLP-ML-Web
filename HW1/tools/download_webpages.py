#!/usr/bin/python
import os
import sys
import urllib
from urllib import *
import bs4
from bs4 import BeautifulSoup
import re

###README
#TODO add description here and to main README.txt




# MetaCritic is a site that posts reviews on movies, tv, games, music, etc.
# This link connects specifically to game reviews for the iPhone/iPad


links_file= open('/users/michellemorales/Desktop/NLP-ML-Web-master/HW1/tools/link-list.txt')
links= links_file.readlines()
cleanLinks= [] # Contains a list of all links to metacritic
        
for item in links:
    if item != "\n":
        cleanLinks.append(item.strip())


for link in cleanLinks[:1]:
    linkList= link.split('/')
    title= linkList[-1]        
    webPage= URLopener().open(link)
    htmlDoc= webPage.read()
    webPage.close()
    soup= BeautifulSoup(htmlDoc)

    outFile= open('../data/train/'+title+'.htm', 'w')
    writeToFile= outFile.write(htmlDoc)
    

