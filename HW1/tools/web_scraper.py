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
fileName = os.path.basename(os.path.normpath(directory))
print fileName
metacritic = "http://www.metacritic.com"

def crawl(webPage):
    print("processing: " + webPage + '\n')

    # Opens link and reads source code
    openPage = URLopener().open(webPage) 
    htmlDoc = openPage.read()
    openPage.close()

    # print htmlDoc

    # Creates a beautifulSoup object
    soup = BeautifulSoup(htmlDoc)

    # Finds all links on webpage
    linkList = []
    for link in soup.find_all('a'):
        linkList.append(link.get('href'))

    # Finds valid links (only links within metacritic)
    validLinks = []
    for link in linkList:
        if 'metacritic' not in link and '.com' in link or 'twitter' in link:
            continue
        else:
            validLinks.append(link)
        
    # Lists all links that must be ignored!
    mc = 'http://www.metacritic.com/'
    mcGame = 'http://www.metacritic.com/game/'
    ignoreList = [mc + 'music', mc + 'tv', mc + 'movie', mcGame + 'pc', mcGame + 'ios', mcGame + 'playstation-3', 
    mcGame + 'xbox', mcGame +'wii-u', mcGame + '3ds', mcGame + 'playstation-vita', mcGame + 'wii', mcGame + 'psp', mcGame + 'legacy']

    # # Random walk through valid links, writes every link that is a review to a new file
    goodLinks = []
    checkAgain = []
    newLinkFile = open(directory + "/" + fileName + "-links.txt", 'w')
    for link in validLinks: 
        if "http" not in link:
            newLink = 'http://www.metacritic.com'+link 
        else:
            newLink = link 
        try:
            followLink = URLopener().open(newLink)
            checkLink = followLink.read()
            soupIt = BeautifulSoup(checkLink)
            if 'Reviews - Metacritic' in soupIt.title.string and 'Metascore' and 'Release Date' and 'User Score' in soupIt.get_text() and newLink not in ignoreList:
                # check if link has a Score
                try:
                    # find SCORE
                    score = int(soupIt.find_all(itemprop="ratingValue")[0].get_text())

                    print "Wrote to file good link: " +  newLink + '\n'
                    newLinkFile.write(newLink + '\n')
                except:
                    print "No score found"

            else: 
                print 'Will check again: ' + newLink + '\n'
                checkAgain.append(newLink)
        except IOError:
            print "Link no longer valid: " + newLink + '\n'
    # Removes duplicates
    checkList = list(set(checkAgain))
    # Shuffle list of links
    random.shuffle(checkList)
    crawl(checkList[0])

crawl(metacritic)