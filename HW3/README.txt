Fall 2013
NLP/ML/WEB by Pr. Andrew Rosenberg

original GitHub URL: https://github.com/grezesf/NLP-ML-Web/tree/master/HW3

This repository contains the work of Michelle Morales and Felix Grezes on homework 3 of this class.
This README file describes the data, files and how to use the tools.

### EXTERNAL LIBRARIES AND TOOLS:
Python 2.6.5 +
Beautiful Soup 4


############################
### INSTRUCTIONS
############################



############################
### FILE DESCRIPTIONS
############################

3a_freebase_query.py

3b_accuracy.py

4a_find_dobs.py

./tools/get_people.py
    We used this script to gather a list of famous people automatically. Uses Freebase API to query and access people and DOBS
    Results are 100 names with DOBs

./tools/split_data.py
    We used this script to split the names of famous people from DOB, then separates the 2 new list into training and testing lists, then writes new lists in files.

./tools/fbook_split.data.py
    We used this script to do the same thing as the script above, on the list of non-famous people.

############################
### HOMEWORK OVERVIEW
############################

Problem 1: famous people.
    We automatically gathered a list of 50 famous people and their birthdates from freebase. This made the subsequent task 3b rather easy, but any list of names should work for that part.

Problem 2: non-famous people
    We manually gathered a list of 50 facebook friends as well as their birthdates.

Problem 3: exploiting structured data
    Since our own list of famous people was obtained from Freebase, our results are perfect. However our script is a general freebase searcher, so any list of names should be compatible.

Problem 4: exploiting unstructured data
    
