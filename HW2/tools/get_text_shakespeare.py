#!/usr/bin/python
import os
import sys
import urllib
from urllib import *
import bs4
from bs4 import BeautifulSoup

###README

# opens current directory
working_dir = '../data/shakespeare/'
print 'opening directory'

# creates new file, to write all text to
new_file = open(working_dir+'/fulldata_shakespeare.txt', 'w')

# opens directory and creates a list of all files, then iterates through each file

for file in os.listdir(working_dir):
    print 'processing first file:' +' '+ file
    text_file = URLopener().open(working_dir + file)
    text = text_file.read()
    soup= BeautifulSoup(text)
    
    # pulls all text from the file and writes it to new file
    for line in soup.find_all('line'):
        new_line = line.get_text()
        new_file.write(new_line + '\n')
        print 'writing to file:' +' '+ new_line
        
new_file.close()
new_file = open(working_dir+'/fulldata_shakespeare.txt','r')

print len(new_file.read().split())




        