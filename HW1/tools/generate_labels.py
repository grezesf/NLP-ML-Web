#!/usr/bin/python
import os
import sys

from bs4 import BeautifulSoup

print '\n'

###README
# this script takes a directory of html pages 
# and outputs the proper training labels in the same dir
# example call: generate_labels.py ../data/train 
# file: www.metacritic.com/movie/pokmon-the-first-movie---mewtwo-strikes-back!
# line in labels file: http:__www.metacritic.com_movie_pokmon-the-first-movie---mewtwo-strikes-back!,MOVIE,BAD,OLD,35,67


# directory containing the html pages
htm_dir = sys.argv[1]
print "directory containing the htm files: " + htm_dir

#directory to save the labels file in (deprecated, used to be one above ie cd .. )
# work_dir = '/'.join(htm_dir.split('/')[:-1])
# print work_dir

# name of label.txt
labels_name = htm_dir.split('/')[-1] + "_labels.txt"
print "name of the labels file to be created: " + labels_name
print '\n'

# create and open labels file
labels = open(htm_dir + '/' + labels_name, 'w+')

# for all html file in the dir
for (path, dirs, files) in os.walk(htm_dir):
    for f in files:
        # only work on .htm files
        if '.htm'in f:
            # print f
            # make soup object
            soup_obj = BeautifulSoup(open(path + '/' + f))

            #link
            page_link = soup_obj.find_all(rel="canonical")[0]['href'].replace('/','_')
            print page_link
            # MEDIA
            media = soup_obj.find("meta")
            # [0]['content'].upper()
            print media
            # GRADE
            # OLD/NEW
            # SCORE
            # score = soup_obj.findAll(<span class="score_value" itemprop="ratingValue">
            # USER-RATINGS

            




# close file
labels.close()