Fall 2013
NLP/ML/WEB by Pr. Andrew Rosenberg

This repository contains the work of Michelle Morales and Felix Grezes on homework 1 of this class.
This README file describes the data, files and how to use the tools.

### EXTERNAL LIBRARIES AND TOOLS:
Beautiful Soup 4 
WEKA 3.7


############################
### INSTRUCTIONS
############################

Make sure to have Weka 3.7 and Beautiful Soup 4 installed. 
run_exp.sh ???????

############################
### FILE DESCRIPTIONS
############################

download_webpages.py
This script reads a text file. The text file contains a list of links from MetaCritic. MetaCritic is a site that posts reviews on movies, tv, games, music, etc. The script reads the file and creates a list of links. It then iterates through the listof links, opening each link, and writing the information pulled from each link into a new file.
# ex: download_pages.py ../data/train/train-links.txt

generate_labels.py
this script takes a directory of html pages and outputs the proper training labels in the same dir
# examples
call: generate_labels.py ../data/train 
file: www.metacritic.com/movie/pokmon-the-first-movie---mewtwo-strikes-back!
line in labels file: http:__www.metacritic.com_movie_pokmon-the-first-movie---mewtwo-strikes-back!,MOVIE,BAD,OLD,35,67

web_scraper.py
This web scraper takes a directory as its one argument. The script contains one function named crawl. Crawl is given 1 argument, which must be a link
The function then does a random walk through the site searching for valid links. In this case valid links would be a link to a specific review. All valid links are written into a new file within the given directory. The function will recursively search exhaustively until all links have been followed.
# ex: web_scraper ../data/dev/

feat_extract.py
This script takes a data directory as input (with the .htm files) and outputs an .arff file with the extracted features in it.
# ex: feat_extract.py ./data/train/
writes: train-feats.arff

run_exp.sh
# This script runs all the experiments performed in Weka for our specific tasks. It calls Weka and creates an experiement folder. Finds and opens all training and testing feature files. Then runs a series of experiments and saves all results into the experiment folder. 

############################
### PROJECT OVERVIEW
############################
Our goal is to extract and build models of various features of the Metacritic.com reviews.
Metacritic.com is a website that aggregates reviews for various media., with the hope of being able to combine them into one single score.

# Data
An instance of our data is a webpage to a single Metacritic media review, e.g. http://www.metacritic.com/movie/seven-samurai .
Our data contains reviews for every type of media available: movies, games, tv shows and music.
Our training data was balanced according to our features, but our test data was not.

# Label Categories
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
	This label is the total number of ratings given by users of Metacritic. It is NOT the user rating score, nor the number of user reviews.
	labels: 0-+inf

#	Our approach
We began by manually balancing our training set to ensure that our training data included a balanced number of examples. 
Then we organically scraped the metacritic website performing a random walk using our web_scraper.py. Labeling was then done automatically using feat_extract.py. The features we extracted were the strings of text pulled from each webpage. We obtained our representations from these features. 

#	Our results
Our results can be reviewed in the table below.  

_______________RESULTS___________________
	                Bag-	Bi-	    Tri-
			        words   gram    gram
			    		        
Media name	        100	    100	    100
Grade	            81.53	94.14	94.14
Old/new	            77.93	77.03	81.98
*_________________________________________*
Score	            0.75	0.49	0.88
Number of Ratings	0.06	-0.16	0.21

*The line separates different result types, above the line (categories-media/grade/oldnew)
results are represented by percentages of correctly classified instances. Below the line
(categories-score/numberofratings) results are represented by the correlation coefficient.

Our results demonstrate that overall performance was improved when moving from a bag-of-words representation to a N-gram representation.
(Detailed results can be viewed in results.txt)


