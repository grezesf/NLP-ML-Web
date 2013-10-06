#!/usr/bin/python
import os
import sys
import urllib
from urllib import *
import bs4
from bs4 import BeautifulSoup
import random

###README
# This web scraper takes a directory as its one argument. The script
# contains one function named crawl. Crawl is given 1 argument, which must be a link
# The function then does a random walk through the site searching for valid links. In this
# case valid links would be a link to a specific review. All valid links are written into
# a new file within the given directory. The function will recursively search exhaustively
# until all links have been followed.
# ex: web_scraper ../data/dev/

# This script takes one argument, the argument should be a directory
directory = sys.argv[1]
fileName = os.path.basename(os.path.normpath(directory)) + "-links.txt"
print "creating: " + directory + '/' + fileName
newLinkFile = open(directory + '/' + fileName, 'w+')

# subfunction that checks if a given link is a review page for a specific movie, game, show, album
def isReview(link):
    # try to open the link        
    try:
        followLink = URLopener().open(link)
        checkLink = followLink.read()
        
        # link works
        soupIt = BeautifulSoup(checkLink)
        
        if 'Reviews - Metacritic' in soupIt.title.string and 'Metascore' and 'Release Date' and 'User Score' in soupIt.get_text() and 'Metacritic Reports' not in soupIt.get_text():
           # check if link has a Score
            try:
                # find SCORE
                score = int(soupIt.find_all(itemprop="ratingValue")[0].get_text())
                return True
            except:
                print "No score found"
                return False
        
    # if we can't open the link
    except IOError:
        print "Link no longer valid: " + link + '\n'
        return False
    


# starting link
metacritic = "http://www.metacritic.com"
print "starting link is: " + "http://www.metacritic.com"


futureLinks = [metacritic]
visitedLinks = []




while futureLinks != []:
    #choose random link to visit
    random.shuffle(futureLinks)
    webPage = futureLinks[0]
    del futureLinks[0]
    visitedLinks.append(webPage)
    print("processing: " + webPage + '\n')
    
    # Opens link and reads source code
    try:
        openPage = URLopener().open(webPage) 
        htmlDoc = openPage.read()
        openPage.close()

        # Creates a beautifulSoup object
        soup = BeautifulSoup(htmlDoc)
    
        # Finds all links on webpage
        linkList = []
        for link in soup.find_all('a'):
            linkList.append(link.get('href'))
    #     print linkList
        
        # Finds valid links (only links within metacritic)
        validLinks = []
        for link in linkList:
            if "http" not in link:
                validLinks.append('http://www.metacritic.com'+link)
            elif 'metacritic.com' in link:
                validLinks.append(link)
    
    #     print validLinks
    
        # go through all non visted valid links, find reviews and continue crawling
        for link in [x for x in validLinks if x not in visitedLinks]:
                # making a list and checking it twice
                if link not in visitedLinks:
                    print "checking if review: " + link
                    # check if link is a review
                    if isReview(link):
                            # add to link list file
                            print "Wrote to file good link: " +  link + '\n'
                            newLinkFile.write(link + '\n')
                            # add to visted links
                            visitedLinks.append(link)
                    else:
                        # add to list of future links
                        print "add link for future visit"
                        futureLinks.append(link)
    except:
        print "Something about the link was wrong, ignore it"   


# close file
newLinkFile.close()
