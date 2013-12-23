Fall 2013
NLP/ML/WEB by Pr. Andrew Rosenberg

original GitHub URL: https://github.com/grezesf/NLP-ML-Web/tree/master/Project

This repository contains the work of Michelle Morales and Felix Grezes on the final project of this class.
This README file describes the data, files and how to use the tools.

### EXTERNAL LIBRARIES AND TOOLS:
Python 2.7 +
Beautiful Soup 4

### FILE DESCRIPTION

/data/
This folder contains the bulk of our data scraped from the web
    master_list.txt: is a list of all the visited links
    site_list.txt: a list of all the StackExchange.com websites. Used by scrape_SE.py
Each sub_folder contains the saved html of the visited page, a txt fle with the link, and the html file of the revisions

/features/
Contains the interesting features extracted from the raw /data/. These files are what the machine learning algorithms used.

/results/
Contains the results from our experiments.

/tools/
Contains our scripts
    average_distribution.py: reads a .dat file containing the age-score points of our data and computes the average at each age
    build_site_list.py: This script displays all the StackExchange sub-categories saved as site_list.txt in /data
    classify.py: This script classifies edits into meaning-preserving and meaning-altering
    date_distribution.py: The use of this script is to find the distribution of date over our data set of questions, it takes a folder of files (each file is a question site html), and prints list of dates and scores
    dictionary.txt: this file is used by our spell checker
    edit_analyzer.py: this script performs a number of statistical analysis of our mean-changing edits
    feat_extract.py: this script extract desired features from the raw data set and converts them to WEKA readable .arff format
    feat_extract_task2.py: this script extract desired features from the raw data set, used for the second part of our experiments
    score_distribution.py: The use of this script is to find the distribution of scores over our data set of questions
    scrape_SE.py: our stackExchange.com web scraper
    plot_*.gp: various gnuplot scripts


### PROJECT OVERVIEW
Stack Exchange question/answer improvements
    The high level idea is to explore the questions and answers of the StackExchange.com website.
    These websites are community driven, allowing anyone to ask questions on a variety of topics.
    Other users then attempt to clarify the question, provide answers and vote for the best ones.

    We have different potential tasks, starting a simply correlating the text, tags and other to 
    a question's upvotes; and more ambitiously suggesting edits to the text, based on past revisions.


   