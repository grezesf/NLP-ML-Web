#!/usr/bin/python
import os
import sys

from bs4 import BeautifulSoup

###README
# this script takes a directory of html pages and outputs the proper training labels
# eg. file: http://www.metacritic.com/movie/pokmon-the-first-movie---mewtwo-strikes-back!
# line in labels file: http:__www.metacritic.com_movie_pokmon-the-first-movie---mewtwo-strikes-back!,MOVIE,BAD,OLD,35,67

htm_dir = sys.argv[1]
print htm_dir