#!/usr/bin/python
import os
import sys
import re

### README
# Reads a file that contains a list of names and DOBS (format YEAR-MONTH-DAY)
# Splits name from DOB and separates the 2 new list into training and testing lists, then
# writes new lists into files

# opens name and DOB file and reads info
data_file = open('../data/fbook_dobs.txt', 'r')
data = data_file.readlines()
print data

# opens training and testing files for names and dobs taken from a list of facebook friends
train_name = open('../data/train/train_unfamous_name.txt', 'w')
train_dob = open('../data/train/train_unfamous_dob.txt', 'w')

test_name = open('../data/test/test_unfamous_name.txt', 'w')
test_dob = open('../data/test/test_unfamous_dob.txt', 'w')

counter = 0

# iterates through each line, formats and writes birthday and name to file
for line in data:
    if 'Birthday'  in line:
        name = line.replace("'s Birthday\n", '')
        print name
        
        counter += 1
        if counter < 40:
            train_name.write(name+'\n')
        else:
            test_name.write(name+'\n')
    elif 'scheduled' in line:
        dob = line.replace("scheduled for ", '').replace('November','11').replace('October','10').replace(',','').replace(' ','-')
        if counter < 40:
            train_dob.write(dob)
        else:
            test_dob.write(dob)
            
        print dob
        
