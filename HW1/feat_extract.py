#!/usr/bin/python
import os
import sys
import re

from bs4 import BeautifulSoup

### PRELIMINARIES
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

# create and open arff file
arff = open(htm_dir + '/' + arff_filename, 'w+')
print "creating: " + htm_dir + '/' + arff_filename

# write the header
arff.write("%% 1. METACRITIC %s database\n"  % (arff_filename))
arff.write("@RELATION metacritic\n\n")

# write the basic attributes
arff.write("@ATTRIBUTE  name string\n")
arff.write("@ATTRIBUTE  MEDIA {MOVIE,GAME,TV,MUSIC}\n")
arff.write("@ATTRIBUTE  GRADE {GOOD,AVERAGE,BAD}\n")
arff.write("@ATTRIBUTE  OLD_NEW {OLD,NEW}\n")
arff.write("@ATTRIBUTE  SCORE numeric\n")
arff.write("@ATTRIBUTE  NUM_RATINGS numeric\n")

# write our own features
arff.write("@ATTRIBUTE  text string\n")

# write data line
arff.write("\n@DATA\n")

# open the labels.txt
labels_file = open(htm_dir + '/' + os.path.basename(os.path.normpath(htm_dir)) + "-labels.txt")

# work over all files 
for line in labels_file:
    # write basic attributes
    [htm_name, media, grade, old_new, score, num_ratings] = line.split(';')
    htm_name = htm_name.replace("http:__",'')
    # remove trailing \n
    num_ratings = num_ratings.replace('\n', '')
    print "working on file: " + htm_name

    # start of feature extraction
    # make soup object from corresponding .htm file
    soup_obj = BeautifulSoup(open(htm_dir + '/' + htm_name + '.htm'))

    # get all the text (including nonsense)
    text = soup_obj.get_text().encode('utf-8')
    # # replace all large spaces, tabs and newlines with a single space
    text = " ".join(text.split())
    # # replace all quotation marks (otherwise might break .arff) with a single space
    # text = " ".join(text.split('\''))
    # remove non-alphanumeric char
    text = re.sub(r'[^a-zA-Z0-9]+', ' ', text)

    # write to arff file
    # arff.write("%s,%s,%s,%s,%s,%s\n" % (htm_name, media, grade, old_new, score, num_ratings))
    arff.write("\'%s\',%s,%s,%s,%s,%s,\'%s\'\n" % (htm_name, media, grade, old_new, score, num_ratings,text))

# close the labels_file
labels_file.close()
# close the aarf file
arff.close()