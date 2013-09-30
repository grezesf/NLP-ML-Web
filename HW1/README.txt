Fall 2013
NLP/ML/WEB by Pr. Andrew Rosenberg

This repository contains the work of Michelle Morales and Felix Grezes on homework 1 of this class.
This README file describes the data, files and how to use the tools.

### EXTERNAL LIBRARIES AND TOOLS:
Beautiful Soup 4 
WEKA 3.7


### INSTRUCTIONS


### FILE DESCRIPTIONS
#	./tools/download_wepages


download_webpages.py
This script reads a text file. The text file contains a list of links from MetaCritic. MetaCritic is a site that posts reviews on movies, tv, games, music, etc. The script reads the file and creates a list of links. It then iterates through the list
of links, opening each link, and writing the information pulled from each link into a new file.


### TASK OVERVIEW
Our goal is to extract and build models of various features of the Metacritic.com reviews.
Metacritic.com is a website that aggregates reviews for various media., with the hope of being able to combine them into one single score.

#	Data
An instance of our data is a webpage to a single Metacritic media review, e.g. http://www.metacritic.com/movie/seven-samurai .
Our data contains reviews for every type of media available: movies, games, tv shows and music.
Our training data was balanced according to our features, but our test data was not.

#	Label Categories
We identified 5 label categories that we deemed interesting to modelize. We tried to vary to types of the labels to make it interesting for the machine learning tools.
Cat1: MEDIA
	This label describes if the page is a movie, music, tv show or game review.
	labels: MOVIE; GAME; TV; MUSIC
Cat2: GRADE
	This label describes the general reaction of the review aggregation. It is represented on the page by the score color (green, yellow red)
	labels: GOOD; AVERAGE; BAD
Cat3: OLD/NEW
	We divided the training data into 2 categories, media from 2000/03, and media from 2010/13. For the training data we only have media from those 6 years.
	labels: OLD; NEW
Cat4: SCORE
	This label is the metascore given to the media by Metacritic. It is out of 100
	labels: 0-100
Cat5: #USER-RATINGS
	This label is the total number of ratings given by users of Metacritic. It is NOT the user rating score.
	labels: 0-+inf

#	Our approach

#	Our results


###TODOs
add links to tools

