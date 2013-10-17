#!/usr/bin/python
import os
import sys
import urllib
from urllib import *
import bs4
from bs4 import BeautifulSoup

###README

# opens current directory
working_dir = '../data/movie_reviews/'
print 'opening directory'

# creates new file, to write all text to
new_file = open(working_dir+'fulldata_movies.txt', 'w')

# opens directory and creates a list of all files, then iterates through each file

for (path, dir, files) in os.walk(working_dir):
    for file in files:
        
        if '.txt' in file:
            print 'processing first file:' +' '+ file        
            text_file = open(path + '/' + file, 'r')
            text = text_file.read()
            new_file.write(text)
            print 'writing to file' + ' ' + text
    

        
new_file.close()
new_file = open(working_dir+'/fulldata_movies.txt','r')
print len(new_file.read().split())




        