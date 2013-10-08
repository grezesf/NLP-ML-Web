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
# to call this file, give it as input the path to the links.text
# ex : python download_pages.py ../data/train/train-links.txt


filename = sys.argv[1]
links_file = open(filename) # Opens text file that contains list of links
print("working on list of link file: " + filename)

# work directory
workdir = '/'.join(filename.split('/')[:-1]) + '/'
print "saving files in: " + workdir + '\n'

links = links_file.readlines()

# Cleans list of all links to metacritic
cleanLinks = [] 
for item in links:
    if item != "\n":
        cleanLinks.append(item.strip())


# Iterates through list of links and prints html source code to file
for link in cleanLinks:
    print("processing: " + link)

#Cleans and formats string
    title = link.replace('http://', '').replace("/", "_")

# Opens each link and reads source code    
    print("title: " + title)         
    webPage = URLopener().open(link) #Opens link
    htmlDoc = webPage.read()
    webPage.close()
    
# Creates and writes to a new file that will contain all the information taken from that link
    outFile = open(workdir + title + '.htm', 'w')
    writeToFile = outFile.write(htmlDoc)
    print("wrote to file: " + workdir + title + '.htm\n')
    outFile.close()
    

