Fall 2013
NLP/ML/WEB by Pr. Andrew Rosenberg

original GitHub URL: https://github.com/grezesf/NLP-ML-Web

This repository contains the work of Michelle Morales and Felix Grezes on homework 1 of this class.
This README file describes the data, files and how to use the tools.

### EXTERNAL LIBRARIES AND TOOLS:
Python 2.6.5 +
Beautiful Soup 4 
WEKA 3.7.1 +


############################
### INSTRUCTIONS
############################

To run the whole experiment:
    = make sure you have Beautiful Soup 4 in your Python library
    = make sure you have Weka 3.7.1 + installed
    = warning! I have not been able to run Weka from the command line on Windows (so use Mac OSX or Linux)

Open run_exp.sh and enter the path to the weka.jar on your computer
    line 10: weka_jar=/enter/path/here/weka.jar

1 - Because the complete data sets are large (>5Mb), we need to download them from the links.
    run the following two commands from /NLP-ML-Web/HW1/
    $ python ./tools/download_webpages.py ./data/train/train-links.txt
    $ python ./tools/download_webpages.py ./data/test/test-links.txt 

2 - Next we have to generate the labels for these files.
    run the following two commands from /NLP-ML-Web/HW1/
    $ python ./tools/generate_labels.py ./data/train
    $ python ./tools/generate_labels.py ./data/test

3 - Finally we extract the text from these pages and format it all in .arff files that will be used by Weka.
    run the following two commands from /NLP-ML-Web/HW1/
    $ python ./feat_extract.py ./data/train
    $ python ./feat_extract.py ./data/test

Alternitavely, you can run preliminaries.sh that does steps 1-3 for you.
    $ sh preliminaries.sh

Because we don't want the graders to run into trouble, we've also included our own feats.arff and labels.txt.
This way the experiments can still be run without access to the Internet, but that is against the spirit of our work. (and it makes the repository much bigger)

Now we can run the machine learning algorithmes and get predictions on the test files. (remember to change the path to your weka.jar)
    run the following command from /NLP-ML-Web/HW1/
    $ sh run_exp.sh

Running run_exp.sh will create a folder in /NLP-ML-Web/HW1/results/ that will hold the models, predictions and statistics for all tasks and sub-tasks.
For a sehll dump of an typical run, see typical-results.txt


############################
### FILE DESCRIPTIONS
############################

web_scraper.py
This web scraper takes a directory as its one argument. The script contains one function named crawl. Crawl is given 1 argument, which must be a link
The function then does a random walk through the site searching for valid links. In this case valid links would be a link to a specific review. All valid links are written into a new file within the given directory. The function will recursively search exhaustively until all links have been followed.
# ex: python web_scraper ../data/dev/

download_webpages.py
This script reads a text file. The text file contains a list of links from MetaCritic. MetaCritic is a site that posts reviews on movies, tv, games, music, etc. The script reads the file and creates a list of links. It then iterates through the listof links, opening each link, and writing the information pulled from each link into a new file.
# ex: python download_pages.py ../data/train/train-links.txt

generate_labels.py
this script takes a directory of html pages and outputs the proper training labels in the same dir
call: python generate_labels.py ../data/train 
file: www.metacritic.com/movie/pokmon-the-first-movie---mewtwo-strikes-back!
line in labels file: http:__www.metacritic.com_movie_pokmon-the-first-movie---mewtwo-strikes-back!,MOVIE,BAD,OLD,35,67

feat_extract.py
this script takes a data directory as input (with the .htm files) (it assumes both the data and labels are in this directory) and output a .arff file with the extracted features in it
ex: python feat_extract.py ./data/train/
writes: train-feats.arff

run_exp.sh
# This script runs all the experiments performed in Weka for our specific tasks. It calls Weka and creates an experiement folder. Finds and opens all training and testing feature files. Then runs a series of experiments and saves all results into the experiment folder. 

conver_predictions.py
this script takes as input a Weka style prediction file 
ex: inst#     actual  predicted error distribution ()
        1     2:GAME     2:GAME       0.333,*0.5,0.167,0 
and the corresponding arff file and outputs a file with predictions as in the homework
ex: http:__www.metacritic.com_game_pc_alien-rage;GAME;GAME,+
it also prints the accuracy for nominal classes, for numeric classes, it only creates a file
this script is only meant to be called by run_exp.shand never manually 


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

#   Our approach
We began by manually balancing our training set to ensure that our training data included a balanced number of examples. 
Then we organically scraped the metacritic website performing a random walk using our web_scraper.py. Labeling was then done automatically using feat_extract.py. The features we extracted were the strings of text pulled from each webpage. We obtained our representations from these features. 

#   Our results
Our results can be reviewed in the table below.
NOTE: since the webpages change all the time, the results depends on when they were downloaded.

_______________RESULTS___________________
                    Bag-    Bi-     Tri-
                    words   gram    gram
                                
Media named         100     100 100
Grade               81.53   94.14   94.14
Old/new             77.93   77.03   81.98
*_________________________________________*
Score               0.75    0.49    0.88
Number of Ratings   0.06    -0.16   0.21

*The line separates different result types, above the line (categories-media/grade/oldnew)
results are represented by percentages of correctly classified instances. Below the line
(categories-score/numberofratings) results are represented by the correlation coefficient.

Our results demonstrate that overall performance was improved when moving from a bag-of-words representation to a N-gram representation.
(Detailed results can be viewed in results.txt)


