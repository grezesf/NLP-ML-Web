#!/usr/bin/python
import os
import sys
import urllib
import random
from bs4 import BeautifulSoup

### README
# This script displays all the StackExchange sub-categories
# saved as site_list.txt in /data

# call: python ./build_sitelist.py > site_list.txt

# website 
url = 'http://www.stackexchange.com/sites'

# opens stack exchange web site
stack_exchange = urllib.urlopen(url).read()

# creates beautiful soup object and gets all the links to topic sites from stack exchange
soup = BeautifulSoup(stack_exchange)
sites = []
for link in soup.findAll('a'):
    site_link = link.get('href')
    sites.append(site_link)
    
# separates the important links (topic site likes) from unimportant ones (twitter, fbook, etc.)
start = sites.index('/sites?view=list')
end = sites.index('/feeds/sites')
# print start, end

# write_file = open('../data/site_list.txt', 'w')

# creates a new list of important links and prints list to file, site_list.txt
important_links = sites[start+1 : end]
# print important_links
for link in important_links:
    # write_file.write(link + '\n')
    print link

# write_file.close()





