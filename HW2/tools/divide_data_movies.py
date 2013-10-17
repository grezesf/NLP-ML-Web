#!/usr/bin/python
import os
import sys
import math




### README


file_path = sys.argv[1]

open_file = open(file_path, 'r')
text = open_file.read()

length = len(text.split())
divider = length * 33.0/100


words = text.split()


train = words[0 : int(math.floor(divider))]


dev = words[int(math.floor(divider)) + 1 : int((2 * math.floor(divider)))]

test = words[int((2 * math.floor(divider))) + 1 :]

 
train_file = open('../data/movie_reviews/movies_train.txt', 'w')
dev_file = open('../data/movie_reviews/movies_dev.txt', 'w')
test_file = open('../data/movie_reviews/movies_test.txt', 'w')

train_file.write(' '.join(train))
dev_file.write(' '.join(dev))
test_file.write(' '.join(test))