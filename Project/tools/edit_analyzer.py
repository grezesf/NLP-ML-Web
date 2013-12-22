#!/usr/bin/python
import os
import sys
from collections import Counter

# README
# this script performs a number of statistical analysis of our mean-changing edits


# edit file 
# should be classify_results3.txt
edit_file_path = os.path.abspath(os.path.normpath(sys.argv[1]))
# open file
edit_file = open(edit_file_path, 'r')
# read lines
edit_lines = edit_file.readlines()

# close file
edit_file.close()

# set counters to zero
dist_list = []
edit_list = []
line_cpt = 1
 
for line in edit_lines:
    # extract values
    # [deletion, addition, distance] = line.split(',')
    # temp_list = line.split(',')
    # print line.split('",')
    # [deletion, addition, distance] = line.split('",')
    # distance = temp_list[-1].strip()
    # print distance
    # print line_cpt

    if (line_cpt % 4) == 0:
        # add distance to list
        dist_list.append(distance)
        # add edits to list
        edit_list.append((deletion, addition, distance))

        # print line_cpt, deletion, addition, distance

    elif (line_cpt % 4) == 1:
        # deletion
        deletion = line.strip()
    elif (line_cpt % 4) == 2:
        # addition
        addition = line.strip()
    elif (line_cpt % 4) == 3:
        # edit distance
        distance = line.strip()


    # increment line_cpt
    line_cpt += 1




# task 1, edit distance count
# file to save counts in
dist_count_file_path = os.path.abspath(os.path.normpath(sys.argv[2]))
dist_count_file = open(dist_count_file_path, 'w')
cnt = Counter(dist_list)
for i in cnt.items():
    # print i[0], i[1]
    dist_count_file.write(i[0] + " " + str(i[1]) + "\n")

# task 2 most common edits
edit_count_file_path = os.path.abspath(os.path.normpath(sys.argv[3]))
edit_count_file = open(edit_count_file_path, 'w')
cnt = Counter(edit_list)
for i in cnt.items():
    # print i[0], i[1]
    # if i[1] >= 2:
    #     print i
    edit_count_file.write(str(i[0]) + " " + str(i[1]) + "\n")

# task 3 find edits that happen more than twice
for i in cnt.items():
    if int(i[0][2]) >= 2 and i[1] >= 2:
        # print i
        print i[0][0] + "   " + i[0][1], i[0][2], i[1]