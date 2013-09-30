#!/usr/bin/python
import os
import sys
import urllib
from urllib import *


###README
# This script reads a text file. The text file contains a list of links from MetaCritic.
# MetaCritic is a site that posts reviews on movies, tv, games, music, etc.
# The script reads the file and creates a list of links. It then iterates through the list
# of links, opening each link, and writing the information pulled from each link into a new file.

filename = 'link-list.txt'
links_file = open(filename) # Opens text file that contains list of links
print("working on list of link file: " + filename)

links = links_file.readlines()

# Cleans list of all links to metacritic
cleanLinks = [] 
for item in links:
    if item != "\n":
        cleanLinks.append(item.strip())


# Iterates through list of links and prints html source code to file
for link in cleanLinks:
    print("processing: " + link)
    linkList = link.split('/')
#Cleans and formats string
    title = str(linkList[4:]).replace('[', '').replace(']','').replace(", ",'+').replace("'",'').strip() 
    
# Opens each link and reads source code    
    print("title: " + title)         
    webPage = URLopener().open(link) #Opens link
    htmlDoc = webPage.read()
    webPage.close()
    
# Creates and writes to a new file that will contain all the information taken from that link
    outFile = open('../data/train/' + title + '.htm', 'w')
    writeToFile = outFile.write(htmlDoc)
    print("wrote to file: " + '../data/train/' + title + '.htm\n')
    

