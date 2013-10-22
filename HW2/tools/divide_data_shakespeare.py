#!/usr/bin/python
import os
import sys
import math

### README
# This script takes as input the path to the large shakespeare data text file
# and divides it into three train, dev and test files

#file containing the shakespeare data
file_path = sys.argv[1]

# open the large text file
open_file = open(file_path, 'r')
text = open_file.read()

# define divider as thirds
length = len(text.split())
divider = length * 33.0/100

# make word list
words = text.split()

# print math.floor(divider)

# make data set as thirds
train = words[0 : int(math.floor(divider))]
dev = words[int(math.floor(divider)) + 1 : int((2 * math.floor(divider)))]
test = words[int((2 * math.floor(divider))) + 1 :]

 
train_file = open('../data/shakespeare/shakespeare_train.txt', 'w')
dev_file = open('../data/shakespeare/shakespeare_dev.txt', 'w')
test_file = open('../data/shakespeare/shakespeare_test.txt', 'w')

train_file.write(' '.join(train))
dev_file.write(' '.join(dev))
test_file.write(' '.join(test))