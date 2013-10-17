#!/usr/bin/python
import os
import sys
import nltk




### README

# opens path and reads corpus in train text file
train_path = '../data/shakespeare/shakespeare_train.txt'
train_file = open(train_path, 'r')
train = train_file.read()

# opens path and reads corpus in dev text file
dev_path = '../data/shakespeare/shakespeare_dev.txt'
dev_file = open(dev_path, 'r')
dev = dev_file.read()


print 'DOMAIN: Shakespeare'

# applies smoothing 
est =  lambda fdist, bins: LidstoneProbDist(fdist, 0.2) 

# creates n-gram language model object using nltk, builds model on train data, calculates perplexity on dev set
for n in range(6)[2:6]:
    model = nltk.model.ngram.NgramModel(n, train, estimator = est)
    perp = model.perplexity(dev.split())
    print 'n-gram language model: n = %d\nperplexity = %.06f' %(n, perp)
    print '\n'

# opens path and reads corpus in train text file
train_path = '../data/movie_reviews/movies_train.txt'
train_file = open(train_path, 'r')
train = train_file.read()

# opens path and reads corpus in dev text file
dev_path = '../data/movie_reviews/movies_dev.txt'
dev_file = open(dev_path, 'r')
dev = dev_file.read()


print 'DOMAIN: Movie Reviews'
# creates n-gram language model object using nltk, builds model on train data, calculates perplexity on dev set
for n in range(6)[2:6]:
    model = nltk.model.ngram.NgramModel(n, train, estimator = est)
    perp = model.perplexity(dev.split())
    print 'n-gram language model: n = %d\n perplexity = %.06f' %(n, perp)
    print '\n'