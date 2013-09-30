#!/usr/bin/python
import os
import sys
import urllib
from urllib import *


###README
#TODO add description here and to main README.txt




# MetaCritic is a site that posts reviews on movies, tv, games, music, etc.
# This link connects specifically to game reviews for the iPhone/iPad


links_file= open('link-list.txt') # Opens text file that contains list of links
links= links_file.readlines()

cleanLinks= [] # Contains a cleaned list of all links to metacritic
for item in links:
    if item != "\n":
        cleanLinks.append(item.strip())


for link in cleanLinks[:1]: #Iterates through list of links and prints html source code to file
    linkList= link.split('/')
    title= linkList[-1]   
         
    webPage= URLopener().open(link)
    htmlDoc= webPage.read()
    webPage.close()
    outFile= open('../data/train/'+title+'.htm', 'w')
    writeToFile= outFile.write(htmlDoc)
    

