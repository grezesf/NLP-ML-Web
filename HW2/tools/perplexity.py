#!/usr/bin/python
import os
import sys
import nltk




### README


# train_path = '../data/shakespeare/shakespeare_train.txt'
# train_file = open(train_path, 'r')
# train = train_file.read()
# 
# dev_path = '../data/shakespeare/shakespeare_dev.txt'
# dev_file = open(dev_path, 'r')
# dev = dev_file.read()
# 
# 
# print 'SHAKESPEARE'
# for n in range(11)[2:]:
#     print n
#     model = nltk.model.ngram.NgramModel(n, train)
#     perp = model.perplexity(dev.split())
#     print perp


train_path = '../data/movie_reviews/movies_train.txt'
train_file = open(train_path, 'r')
train = train_file.read()

dev_path = '../data/movie_reviews/movies_dev.txt'
dev_file = open(dev_path, 'r')
dev = dev_file.read()

print 'MOVIES'
for n in range(11)[2:]:
    print n
    model = nltk.model.ngram.NgramModel(n, train)
    perp = model.perplexity(dev.split())
    print perp