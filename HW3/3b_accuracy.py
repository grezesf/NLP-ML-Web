#!/usr/bin/python
import os
import sys

### README
# determines accuracy, by comparing found DOBs (found_dobs.txt) with actual date of births (train_dob.txt)
# as input it takes paths to the two files

# this work corresponds to part 3.b of the homework

# open files
# should be './data/train/train_dob.txt' and './data/found_dobs.txt'
actual_data = open (sys.argv[1], 'r')
found_data = open (sys.argv[2], 'r')

# read the lines
actual = actual_data.readlines()
found = found_data.readlines()

# number of DOB
total = len(actual)

# finds accuracy for full DOB
right_count = 0.0
for date in found:
    index = found.index(date)
    date_split = date.split('-') 
    if date == actual[index]:
        right_count += 1.0
   
percent = right_count / total
print 'Accuracy (Full DOB) = ' , percent*100, '%'


# finds accuracy for month and year of DOB
right_count = 0.0
for date in found:
    index = found.index(date)
    date_split = date.split('-') 
    if date_split[1:] == actual[index].split('-')[1:]:
        right_count += 1.0
   
percent = right_count / total
print 'Accuracy (Month & Year) = ' , percent*100, '%'


# finds accuracy for only year of DOB
right_count = 0.0
for date in found:
    index = found.index(date)
    date_split = date.split('-') 
    if date_split[-1] == actual[index].split('-')[-1]:
        right_count += 1.0
   
percent = right_count / total
print 'Accuracy (Year) = ' , percent*100, '%'
            
    