#!/usr/bin/python
import os
import sys
import nltk

from nltk.probability import LaplaceProbDist


### NLP-ML-Web: Homework 2
# Michelle Morales & Felix Grezes

# max size of ngrams
max_n = 6


# Problem 1
# 1.a
# Domain A is Movie Reviews (NLTK dataset)
# see /data/get_text_movies.py and /data/divide_data_movies.py
# data is divided into thirds. 33% train 33% dev 33% test

print '1.a DOMAIN A: Movie Reviews'

# opens path and reads corpus in train text file
movies_train_path = './data/movie_reviews/movies_train.txt'
movies_train_file = open(movies_train_path, 'r')
movies_train = movies_train_file.read()

# opens path and reads corpus in dev text file
movies_dev_path = './data/movie_reviews/movies_dev.txt'
movies_dev_file = open(movies_dev_path, 'r')
movies_dev = movies_dev_file.read()

# 1.b
# crashes because of lack of smoothing and/or NLTK bugs

# 1.c
print "1.c Smoothing"

# shorten for dev purposes
# movies_train = movies_train[0:1000]
# movies_dev = movies_dev[0:1000]

# make word list
movies_train_words = nltk.word_tokenize(movies_train)
movies_dev_words = nltk.word_tokenize(movies_dev)

# smoothing function
print "Smoothing function: LaPlace"
est =  lambda fdist, bins: LaplaceProbDist(fdist, bins=None) 


movies_best_perp = "not set"

# creates n-gram language model object using nltk, builds model on train data, calculates perplexity on dev set
for n in range(max_n)[2:11]:
    print "training %d-gram language model" % (n)

    # build n-gram
    movies_train_ngrams = nltk.ngrams(movies_train_words, n, False, True)

    # train model
    movies_model = nltk.model.ngram.NgramModel(n, movies_train_ngrams, estimator = est)
    # model = nltk.model.ngram.NgramModel(n, train_ngrams)
    print "training finished, calculating perplexity"
    movies_train_perp = movies_model.perplexity(movies_train_words)
    print 'train set perplexity = %.06f' % (movies_train_perp)
    movies_dev_perp = movies_model.perplexity(movies_dev_words)
    print 'dev set perplexity = %.06f' % (movies_dev_perp)
    
    if movies_best_perp == "not set" or movies_dev_perp<movies_best_perp:
        print "found new best model"
        movies_best_n = n
        movies_best_perp = movies_dev_perp
        movies_best_model = movies_model

    print 

# test the best model on test set
print "Best N:" , movies_best_n
# opens path and reads corpus in test text file
movies_test_path = './data/movie_reviews/movies_test.txt'
movies_test_file = open(movies_test_path, 'r')
movies_test = movies_test_file.read()

# shorten for dev purposes
# movies_test = movies_test[0:1000]

# make word list
movies_test_words = nltk.word_tokenize(movies_test)

# evaluate model
movies_test_perp = movies_best_model.perplexity(movies_test_words)
print 'Domain A test set perplexity = %.06f' % (movies_test_perp)
print


# 1.d




# 2.a
# Domain B is Shakespeare plays (NLTK dataset)
# see /data/get_text_shakespeare.py and /data/divide_data_shakespeare.py
# data is divided into thirds. 33% train 33% dev 33% test

print '2.a DOMAIN B: Shakespeare plays'

# opens path and reads corpus in train text file
shakespeare_train_path = './data/shakespeare/shakespeare_train.txt'
shakespeare_train_file = open(shakespeare_train_path, 'r')
shakespeare_train = shakespeare_train_file.read()

# opens path and reads corpus in dev text file
shakespeare_dev_path = './data/shakespeare/shakespeare_dev.txt'
shakespeare_dev_file = open(shakespeare_dev_path, 'r')
shakespeare_dev = shakespeare_dev_file.read()

# shorten for dev purposes
# shakespeare_train = shakespeare_train[0:1000]
# shakespeare_dev = shakespeare_dev[0:1000]

# make word list
shakespeare_train_words = nltk.word_tokenize(shakespeare_train)
shakespeare_dev_words = nltk.word_tokenize(shakespeare_dev)

# 2.b
print "2.b"

# smoothing function
print "Smoothing function: LaPlace"
est =  lambda fdist, bins: LaplaceProbDist(fdist, bins=None) 


shakespeare_best_perp = "not set"

# creates n-gram language model object using nltk, builds model on train data, calculates perplexity on dev set
for n in range(max_n)[2:11]:
    print "training %d-gram language model" % (n)

    # build n-gram
    shakespeare_train_ngrams = nltk.ngrams(shakespeare_train_words, n, False, True)

    # train model
    shakespeare_model = nltk.model.ngram.NgramModel(n, shakespeare_train_ngrams, estimator = est)
    # model = nltk.model.ngram.NgramModel(n, train_ngrams)
    print "training finished, calculating perplexity"
    shakespeare_train_perp = shakespeare_model.perplexity(shakespeare_train_words)
    print 'train set perplexity = %.06f' % (shakespeare_train_perp)
    shakespeare_dev_perp = shakespeare_model.perplexity(shakespeare_dev_words)
    print 'dev set perplexity = %.06f' % (shakespeare_dev_perp)
    
    if shakespeare_best_perp == "not set" or shakespeare_dev_perp<shakespeare_best_perp:
        print "found new best model"
        shakespeare_best_n = n
        shakespeare_best_perp = shakespeare_dev_perp
        shakespeare_best_model = shakespeare_model

    print 

# test the best model on test set
print "Best N:" , shakespeare_best_n
# opens path and reads corpus in test text file
shakespeare_test_path = './data/shakespeare/shakespeare_test.txt'
shakespeare_test_file = open(shakespeare_test_path, 'r')
shakespeare_test = shakespeare_test_file.read()

# shorten for dev purposes
# shakespeare_test = shakespeare_test[0:1000]

# make word list
shakespeare_test_words = nltk.word_tokenize(shakespeare_test)

# evaluate model
shakespeare_test_perp = shakespeare_model.perplexity(shakespeare_test_words)
print 'Domain B test set perplexity = %.06f' % (shakespeare_test_perp)
print


# 2.c
print "2.c Cross domain evaluation"

cross_perp_1 = movies_best_model.perplexity(shakespeare_test_words)
cross_perp_2 = shakespeare_best_model.perplexity(movies_test_words)
print "best movie model perplexity on cross domain test set = %.06f" % (cross_perp_1)
print "best Sheakespeare model perplexity on cross domain test set = %.06f" % (cross_perp_2)

