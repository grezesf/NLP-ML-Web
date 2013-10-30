Fall 2013
NLP/ML/WEB by Pr. Andrew Rosenberg

original GitHub URL: https://github.com/grezesf/NLP-ML-Web/tree/master/HW3

This repository contains the work of Michelle Morales and Felix Grezes on homework 3 of this class.
This README file describes the data, files and how to use the tools.

### EXTERNAL LIBRARIES AND TOOLS:
Python 2.7 +
Beautiful Soup 4


############################
### INSTRUCTIONS
############################
!!ATTENTION!!
Unlike previous homeworks, this one requires Python 2.7 or above (not just 2.6.5) since we are using the collections library.

The three scripts to run are:
3a_freebase_query.py
3b_accuracy.py
4a_find_dobs.py (this ones takes too long)

############################
### FILE DESCRIPTIONS
############################

3a_freebase_query.py
    # Takes a list of names as input, creates a freebase query, and returns the date of birth of the query
    # also takes as input a path to where the output file will be saved
    # ex: python 3a_freebase_query.py ./data/train/train_name.txt ./data/train/train_dobs.txt

3b_accuracy.py
    # determines accuracy, by comparing found DOBs (found_dobs.txt) with actual date of births (train_dob.txt)
    # as input it takes paths to the two files

4a_find_dobs.py
    # takes a list of names and uses unstructured data to find DOBs
    # as input it takes a patch to a list of names and a path to the results file

./tools/get_people.py
    We used this script to gather a list of famous people automatically. Uses Freebase API to query and access people and DOBS
    Results are 100 names with DOBs

./tools/split_data.py
    We used this script to split the names of famous people from DOB, then separates the 2 new list into training and testing lists, then writes new lists in files.

./tools/fbook_split.data.py
    We used this script to do the same thing as the script above, on the list of non-famous people.

./get_dates.py
    The code for this script comes from this answer on stackoverflow
    http://stackoverflow.com/questions/6562148/python-finding-date-in-a-string
    We use it find date patterns in the text we extract form webpages.

############################
### HOMEWORK OVERVIEW
############################

Problem 1: famous people.
    We automatically gathered a list of 50 famous people and their birthdates from freebase. This made the subsequent task 3b rather easy, but any list of names should work for that part.

Problem 2: non-famous people
    We manually gathered a list of 50 facebook friends as well as their birthdates.

Problem 3: exploiting structured data
    Since our own list of famous people was obtained from Freebase, our results are perfect.However our script is a general freebase searcher, so any list of names should be compatible.
    Our results can be seen in 3b_results.txt

Problem 4: exploiting unstructured data
    We created a list of 50 unfamous people (our friends) and their birthdays.
    Our strategy for finding their birthday on unstructured web data is as follow:
        Search their name in Yahoo search (google or bing was more difficult and/or obfusctated)
        Peruse the links found, and if the text in those links finds the name and one of the keywords ('birth', 'birthday', 'dob', 'born'), then parse the text for anything that looks like a date.
        Eliminate dates that are too old (before 1960() or too late (after 2010) as those are unlikely to be birthday's of people with a web presence.
        Our prediction is the date that appeared the most often within these criterias.

    Notes on this proble;:
    Obviously this strategy if very rough, the script runs for a long time and in a lot of cases it does not find any good dates, in which case we just write a blank.

    Our predictions can be found in:
    4a_pred_train.txt
    As can be seen when comparing with /data/train/train_unfamous_dob.txt, we only get close to one birth date (line 18, Michael Bush). I believe it to be very difficult just to identify a person with just there first and last name (culturaly dependent), even more to succesfully extract their birthday.

    4a_pred_test.txt (currently computing)
