#!/usr/bin/python
import os
import sys
import re

from bs4 import BeautifulSoup

# newline for shell readability
print '\n'

###README
# this script takes a directory of html pages 
# and outputs the proper training labels in the same dir
# examples
# call: generate_labels.py ../data/train 
# file: www.metacritic.com/movie/pokmon-the-first-movie---mewtwo-strikes-back!
# line in labels file: http:__www.metacritic.com_movie_pokmon-the-first-movie---mewtwo-strikes-back!,MOVIE,BAD,OLD,35,67


# directory containing the html pages
htm_dir = sys.argv[1]
print "directory containing the .htm files: " + htm_dir

#directory to save the labels file in (deprecated, used to be one above ie cd .. )
# work_dir = '/'.join(htm_dir.split('/')[:-1])
# print work_dir

# name of label.txt
labels_name = os.path.basename(os.path.normpath(htm_dir)) + "-labels.txt"
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
            page_link = 'http:__' + f.rstrip('.htm')
            print page_link

            # extract the labels
            # ALL the following are rather ugly hacks
            # MEDIA
            media = page_link.split('_')[3].upper()
            print "media: " , media
            # OLD/NEW
            if media == "TV":
                date = soup_obj.get_text()
                regexp = re.search( '\d, 20\d\d', date).group(0)
                date = regexp[-4:]
                if  int(date) <= 2006:
                    date = "OLD"
                else:
                    date = "NEW"
            else:
                date = soup_obj.find_all(itemprop="datePublished")[0].get_text().strip()
                date = date[-4:]
                if int(date) <= 2006:
                    date = "OLD"
                else:
                    date = "NEW"
            print "OLD/NEW: " , date
            # SCORE
            score = int(soup_obj.find_all(itemprop="ratingValue")[0].get_text())
            print "Score: " , score
            # USER-RATINGS
            num_ratings = soup_obj.strong
            if num_ratings == None:
                num_ratings = 0
            else:
                num_ratings = int(num_ratings.get_text()[:-8])
            print "#RATINGS: " , num_ratings
            # GRADE
            if media == "GAMES":
                if score >= 75:
                    grade = "GOOD"
                elif score >= 50:
                    grade = "AVERAGE"
                else:
                    grade = "BAD"
            else:
                if score >= 61:
                    grade = "GOOD"
                elif score >= 40:
                    grade = "AVERAGE"
                else:
                    grade = "BAD"
            print "GRADE :" , grade

            print '\n'
            

            # write to file
            labels.write("%s;%s;%s;%s;%d;%d\n" % (page_link, media, grade, date, score, num_ratings))


# close file
labels.close()