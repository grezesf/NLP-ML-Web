Fall 2013
NLP/ML/WEB by Pr. Andrew Rosenberg

original GitHub URL: https://github.com/grezesf/NLP-ML-Web/tree/master/Project

This repository contains the work of Michelle Morales and Felix Grezes on the final project of this class.
This README file describes the data, files and how to use the tools.

### EXTERNAL LIBRARIES AND TOOLS:
Python 2.7 +
Beautiful Soup 4


### PROJECT OVERVIEW
Stack Exchange question/answer improvements
    The high level idea is to explore the questions and answers of the StackExchange.com website.
    These websites are community driven, allowing anyone to ask questions on a variety of topics.
    Other users then attempt to clarify the question, provide answers and vote for the best ones.

    We have different potential tasks, starting a simply correlating the text, tags and other to 
    a question's upvotes; and more ambitiously suggesting edits to the text, based on past revisions.


    * Task 1: Features - Rank/Score correlation
Before anything useful can be done, we need to know what features can be useful for our tasks.

Step 1: build data
build_site_list.py (done)
    tiny script that finds all the Stack Exchange sub-websites
scrape_SE.py
    script that explores and saves the raw html of question links. Adds (not replaces) to the current dataset.
    input: latest list of links
feat_extract.py
    script that build the .arff from the above raw data
    input: folder containing the raw html

Features to extract
    Possible targets:
        vote-count-post (aka score) (for both)
        normalized score (to define) (for both)

        favoritecount (questions only)
        number of answers (questions only)

        Rank (answers only)
        vote-accepted-on (if the question owner accepted this answer) (answers only)

    Possible features:
        text

    * Sub-task 1.1: Data exploration: Normalized score
        How does the score (vote-count-post) depend on how old the question/answers is?
        re-score by average? median? threshold?
