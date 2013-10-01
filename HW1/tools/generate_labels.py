#!/usr/bin/python
import os
import sys

from bs4 import BeautifulSoup

###README
# this script takes a directory of html pages 
# and outputs the proper training labels in the same dir
# example call: generate_labels.py ../data/train 
# file: www.metacritic.com/movie/pokmon-the-first-movie---mewtwo-strikes-back!
# line in labels file: http:__www.metacritic.com_movie_pokmon-the-first-movie---mewtwo-strikes-back!,MOVIE,BAD,OLD,35,67


# directory containing the html pages
htm_dir = sys.argv[1]
print htm_dir

#directory to save the labels file in (deprecated, used to be one above)
# work_dir = '/'.join(htm_dir.split('/')[:-1])
# print work_dir

# name of label.txt
labels_name = htm_dir.split('/')[-1] + "_labels.txt"
print labels_name

# create and open labels file
labels = open(htm_dir + '/' + labels_name)