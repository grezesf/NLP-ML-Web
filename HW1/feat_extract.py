#!/usr/bin/python
import os
import sys

from bs4 import BeautifulSoup

# newline for shell readability
print '\n'

###README
# this script takes a data directory as input (with the .htm files)
# and output a .arff file with the extracted features in it
# ex: feat_extract.py ./data/train/
# writes: train-feats.arff

# work directory
htm_dir = sys.argv[1]
print "working in: " + htm_dir

# arff file name
arff_filename =  os.path.basename(os.path.normpath(htm_dir)) + "-feats.arff"

# create and open labels file
labels = open(htm_dir + '/' + arff_filename, 'w+')
print "creating: " + htm_dir + '/' + arff_filename

# for all html file in the dir
for (path, dirs, files) in os.walk(htm_dir):
    for f in files:
        # only work on .htm files
        if 'mask.htm'in f:
            print f
            # make soup object
            soup_obj = BeautifulSoup(open(path + '/' + f))
            # extract text that we care about

            # print soup_obj.get_text().encode('utf-8').strip()
            # reviews = soup_obj.find_all(="review_body")
            # print len(reviews)
            # print reviews.get_text().encode('utf-8').strip()

# close the aarf file
labels.close()