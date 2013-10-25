#!/usr/bin/python
import os
import sys
import urllib
from bs4 import BeautifulSoup

### README
# takes a list of names and uses unstructured data to find DOBs

# opens search url(yahoo)
url = 'http://search.yahoo.com/search?p=Kristina%20Sarceno'
soup = BeautifulSoup(urllib.urlopen(url).read())


search_links = []

for tag in soup.find_all('a'):
    link = tag.get('href')
    search_links.append(link)

all_text = []
for link in search_links[:100]:
    print 'processing link... ' + link + '\n'
    try:
        soup = BeautifulSoup(urllib.urlopen(link).read())
        text = soup.get_text()
        if 'Sarceno' in text and 'search' not in link:
            print 'Sarceno in text: ' + link + '\n'
            all_text.append(text)
            
    except:
        print 'Link not valid: ' + link + '\n'



for text in all_text:
    print text

print len(all_text)