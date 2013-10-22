Fall 2013
NLP/ML/WEB by Pr. Andrew Rosenberg

original GitHub URL: https://github.com/grezesf/NLP-ML-Web/tree/master/HW2

This repository contains the work of Michelle Morales and Felix Grezes on homework 2 of this class.
This README file describes the data, files and how to use the tools.

### EXTERNAL LIBRARIES AND TOOLS:
Python 2.6.5 +
Beautiful Soup 4
NLTK


############################
### INSTRUCTIONS
############################

To run the experiment, run hw2.py. This will run through each of the implemented parts of the homework.
The data set are pretty large and the scripts might run out memory if run on a laptop.
As is, the scripts only runs with a reduced data set of 1000 words in each of train, dev and test.
For the whole data, uncomment the "# shorten for dev purposes" lines.

The two output files: small-output.txt and large-output.txt are example outputs of hw2.py, respectively with the reduced and full dataset. 


############################
### FILE DESCRIPTIONS
############################

hw2.py
    this script runs through all the homework assignements. It shows all the results in the command line and does not produce any results file.

get_data_movies
get_data_shakespeare
    these scripts will take the raw NLKT data sets, in XML form for the Shakespeare plays and in another form for the movie reviews. and transforms them into a large txt file containing all the text. For the plays, only the actual spoken dialogues were used.

divide_data_movies
divide_data_shakespeare
    these scripts take the previously created large text files and divides them into thirds for train, dev and test purposes.


############################
### HOMEWORK OVERVIEW
############################

For this homework we chose to use NLTK as our toolkit, which proved to be a poor choice (as explained further). However it did provide us with the two datasets we used. For our large Domain A set, we chose the movie reviews and for the slightly smaller Domain B set, scripts of 5 Shakespeare plays.
These two sets were chosen because we thought the language models between each domain should be very different, given the large time gap.

As previously mentioned, NLTK was a poor choice for this assignment. As it turns out, NLTK's implementation of numerous smoothing techniques are flawed, most notably GoodTuring; and this despite NTLK's popularity. In our work we tried to avoid the bugged functions.

