#!/usr/bin/python

import os
import sys
from bs4 import BeautifulSoup
from collections import Counter



### README
# The use of this script is to find the distribution of scores over our data set of questions, it takes
# a folder of files (each file is a question site html), and prints list of score count
# only looks at questions (for now)
# data used for preliminary data exploration

# path to data
data_path = os.path.abspath(os.path.normpath(sys.argv[1]))

# score_list starts empty
score_list = []

cpt = 0
max_cpt = 10000
# walk the directories
for (path, dirs, files) in os.walk(data_path):
    for file in files:
        # print "working on " + file
        # look at .html not revisions
        if ".html" in file and "revisions" not in file and cpt<max_cpt:
            cpt += 1
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

                # add score to list
                score_list.append(int(score))


            except:
                continue
                # print file

cnt = Counter(score_list)
for i in cnt.items():
    print i[0], i[1]