#!/usr/bin/python
import os
import sys
from bs4 import BeautifulSoup
import datetime
import re

# README
# TASK 2- CLASSIFYING EDITS
# this script extract desired features from the raw data set
# and converts them to WEKA readable .arff format
# input:  data directory
# output: text file with edit pairs 
       

# main function
def main ():

    # directory containing the raw .html files
    raw_data_dir = os.path.abspath(os.path.normpath(sys.argv[1]))
    print raw_data_dir

    # file to save results in
    edits_file = open(os.path.abspath(os.path.normpath(sys.argv[2])), 'w+')


    # walk the directory for data files
    counter = 1
    for (path, dirs, files) in os.walk(raw_data_dir):
        for f in files:
            # work on .html files thatare revisions
            if "revision" in f:

                # open file
                with open(path + '/' + f, 'r') as open_f:
                    f_soup =  BeautifulSoup(open_f)

                    # find additions and deletions
                    revisions = f_soup.find_all("div", {"class" : "post-text inline-diff"})
                    for r in revisions:
                        revs = r.find_all("span", {"class" : re.compile("diff-")})
                        if len(revs) > 1:
                            for i in revs[:-1]:
                                index = revs.index(i)
                                following_i = revs[index + 1]

                                # extract stings
                                if i['class']  == ['diff-delete'] and following_i['class'] == ['diff-add']:
                                    delete = i.getText().encode('ascii', 'ignore').replace("\n", " ")
                                    add = following_i.getText().encode('ascii', 'ignore').replace("\n", " ")
                                    print 'edit pair', counter
                                    print 'writing to file, deletion' + delete
                                    print 'writing to file, addition' + add
                                    
                                    edits_file.write('DELETION ' + str(counter) +': ' + delete + '\n')
                                    edits_file.write('ADDITION ' + str(counter) +': ' + add + '\n')
                                    counter += 1


    return None





# Call to main 
if __name__=='__main__':
    main()


