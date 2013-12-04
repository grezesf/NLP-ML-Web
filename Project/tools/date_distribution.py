#!/usr/bin/python

import os
import sys
from bs4 import BeautifulSoup
from datetime import datetime


### README
# The use of this script is to find the distribution of date over our data set of questions, it takes
# a folder of files (each file is a question site html), and prints list of dates and scores
# only looks at questions (for now)
# data used for preliminary data exploration
# we extract date and score for comparison, and for normalization reasons

# path to data
data_path = os.path.abspath(os.path.normpath(sys.argv[1]))

# walk the directories
for (path, dirs, files) in os.walk(data_path):
    for file in files:
        # print "working on " + file
        # look at .html not revisions
        if ".html" in file and "revisions" not in file:
            # print "working on " + file
            # open file
            f = open(path + '/' + file)
            # make soup object
            soup = BeautifulSoup(f)
            # close file
            f.close()


            try:
                # find score
                # its the first of the vote-count-post
                score = soup.find("span", {"class":"vote-count-post "}).getText()

                # print score

                # find date
                # look at appropriate tags
                for e in soup.find_all("div", {"class" : "user-action-time"}):
                    if 'asked' in e.getText():
                        # this is SO ugly, but it works
                        date = datetime.strptime(BeautifulSoup(str(e)).find("span").get("title"), "%Y-%m-%d %XZ")
                        
                # print type(date)

                today = date.today()

                # calculate the age of the post, in days
                delta = today-date
                age = delta.days
                # print today, date, age
            
                print age, score

            except:
                print file