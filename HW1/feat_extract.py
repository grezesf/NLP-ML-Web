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
arff.write("%%ATRIBUTE name string\n")
arff.write("%%ATRIBUTE MEDIA {MOVIE,GAME,TV,MUSIC}\n")
arff.write("%%ATRIBUTE GRADE {GOOD,AVERAGE,BAD}\n")
arff.write("%%ATRIBUTE OLD-NEW {OLD,NEW}\n")
arff.write("%%ATRIBUTE SCORE numeric\n")
arff.write("%%ATRIBUTE NUM-RATINGS numeric\n")

# write our own features
arff.write("%%ATRIBUTE text string\n")

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
    arff.write("%s,%s,%s,%s,%s,%s,\'%s\'\n" % (htm_name, media, grade, old_new, score, num_ratings,text))

    


# for all html file in the dir
# for (path, dirs, files) in os.walk(htm_dir):
#     for f in files:
#         # only work on .htm files
#         if 'mask.htm'in f:
#             print f
#             # make soup object
#             soup_obj = BeautifulSoup(open(path + '/' + f))

#             # this does in fact give you the review text it just also includes, nonsense
#             # source code, perhaps the best way is just to format the output
#             text_lines = soup_obj.get_text().encode('utf-8').strip().split("\n")
            

#             # iterates through the all the text, and pulls out the good stuff, ignoring nonsense
#             # i believe a good measure would be to start at 'release date' and end at 'see all user reviews'
#             start = 0
#             end = 0
#             for line in text_lines:
#                 if line == "Release Date:" :
#                     index = text_lines.index(line)
#                     start += index
#                 elif "See all" in line and "User Reviews" in line:
#                     index =  text_lines.index(line)
#                     end += index
                    
#             # cleans list, removes duplicate  empty string items, and removes white space
#             clean_list = []
#             for i in list(set(text_lines[start : end + 1])):
#                 clean_list.append(i.strip())
                
#             # joins list into one string of text
#             important_text = '\n'.join(clean_list)
#             print important_text
            
  
#             # print soup_obj.get_text().encode('utf-8').strip()
#             # reviews = soup_obj.find_all(="review_body")
#             # print len(reviews)
#             # print reviews.get_text().encode('utf-8').strip()


# close the labels_file
labels_file.close()
# close the aarf file
arff.close()