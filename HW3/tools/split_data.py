#!/usr/bin/python
import os
import sys
import re

### README
# Reads a file that contains a list of names and DOBS (format YEAR-MONTH-DAY)
# Splits name from DOB and separates the 2 new list into training and testing lists, then
# writes new lists into files

# opens name and DOB file and reads info
data_file = open('../data/names_dobs.txt', 'r')
data = data_file.readlines()
print data

# iterates through each line and splits name from DOB, then reformats DOB

train_name = open('../data/train/train_name.txt', 'w')
train_dob = open('../data/train/train_dob.txt', 'w')

test_name = open('../data/test/test_name.txt', 'w')
test_dob = open('../data/test/test_dob.txt', 'w')

counter = 0

# iterates through info in file
for line in data[:50]:

    #splits name from DOB
    line_list = line.split()
    name = ' '.join(line_list[:-1])
    print name
    
    #writes 40 names into training file and 10 names into testing
    if counter < 40:
        train_name.write(name+'\n')      
    else:
        test_name.write(name+'\n')
    
    #reformats the date of birth then writes into training and testing files
    dob = line_list[-1]
    dob_list = dob.split('-')
    if len(dob_list) == 1:
        new_dob = '-'.join(['xx','xx',dob_list[0]])
        print new_dob
        if counter < 40:
            train_dob.write(new_dob+'\n')   
        else:
            test_dob.write(new_dob+'\n')
    else:
        new_dob = '-'.join([dob_list[-1], dob_list[1], dob_list[0]])
        print new_dob
        if counter < 40:
            train_dob.write(new_dob+'\n')
        else:
            test_dob.write(new_dob+'\n')
    counter += 1
    
    