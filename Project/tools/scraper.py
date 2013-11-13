#!/usr/bin/python
import os
import sys
import random

# ../data/full/quest1/2files+edits
# master txt link list
# format = <site>_quest_number.txt9(.html or .edit1.html)

# opens site_list.txt and reads list of links
file_list = open('../data/site_list.txt', 'r').readlines
site_list = file_list.readlines()

# 