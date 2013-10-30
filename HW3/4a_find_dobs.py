#!/usr/bin/python
import os
import sys
import urllib
from bs4 import BeautifulSoup
from get_dates import find_dates
import datetime
from collections import Counter

### README
# takes a list of names and uses unstructured data to find DOBs
# as input it takes a patch to a list of names and a path to the results file

# open list of names and make it a nice list
names_list = [name.strip() for name in open(sys.argv[1], 'r').readlines()]
# print names_list

# define a list of keywords links to birdates
keywords = ['birth', 'birthday', 'dob', 'born']

# file which to save the DOB predictions
dobs_file = open(sys.argv[2], 'w')

for name in names_list:
    # opens search url(yahoo) and creates beautiful soup object
    list_of_names = name.split()
    print list_of_names
    name_string = name.replace(' ', '%20')
    # print name_string
    url = 'http://search.yahoo.com/search?p=' + name_string
    soup = BeautifulSoup(urllib.urlopen(url).read())


    search_links = []
    # searches through all a tags and finds all hrefs(links). saves link to the link list
    for tag in soup.find_all('a'):
        link = tag.get('href')
        search_links.append(link)

    # initialize some variables
    all_dates = []
    # visited links
    visited_links = []

    # opens every link, makes a beautiful soup object, and searches for person's name within text
    # skip the first links, as they are always useless
    for link in search_links[20:200]:
        # ignore search links (and already visited links)
        if 'search' not in link and link not in visited_links:
            visited_links.append(link)
            print 'processing link: ' + link
            try:
                soup = BeautifulSoup(urllib.urlopen(link).read())
                text = soup.get_text()
                # check if any of the names are in text and if any of the keywords are as well
                if any(name in text for name in list_of_names) and any(keyword in text for keyword in keywords):
                    print 'link has name and keyword, parsing for dates:'
                    # find the dates
                    # try:
                    found_dates = find_dates(text, max_tokens=50 , allow_overlapping=True)
                    for a_date in found_dates:
                        print a_date.date()
                        all_dates.append(a_date.date())
                    # except:
                        # print 'Error parsing for dates'
            except:
                continue
                print 'Link not valid: ' + link
            print '\n'


    # searches for dates
    # # print "text size: " , len(all_text)
    # all_dates = []
    # # print all_text
    # for string in all_text:
    #     # print len(string)
    #     try:
    #         # the string might be too large in which case, just skip it
    #         for a_date in find_dates(string, max_tokens=50 , allow_overlapping=True):
    #             # print a_date,a_date.date()
    #             all_dates.append(a_date.date())
    #     except:
    #         print 'Errors finding dates'



    # heuristic to make a date prediction
    # remove dates from 2010 and later
    all_dates = [a_date for a_date in all_dates if a_date<datetime.date(2010,1,1)]
    # remove dates from before 1960
    all_dates = [a_date for a_date in all_dates if a_date>=datetime.date(1960,1,1)]
    

    # make prediction by number of counts
    if len(all_dates) > 0:
        dob = Counter(all_dates).most_common(1)
        dob = dob[0][0].strftime('%d-%m-%Y')
        print 'DoB prediction: ', dob
        dobs_file.write(dob + '\n')
    else:
        print 'No birthday found!\n'
        dobs_file.write('xx-xx-xxxx\n')

# close files
dobs_file.close()