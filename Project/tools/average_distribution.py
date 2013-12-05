#!/usr/bin/python

import os
import sys

### README
# this script read a .dat file containing the age-score points of our data
# and computes the average at each age

# path to data
data_path = os.path.abspath(os.path.normpath(sys.argv[1]))

# open the file
with open(data_path, 'r') as f:
    read_data = f.readlines()

    # create dictionary of type
    # age:[sum of instances, number of instances]

    # create emtpy dictionary
    age_dict = {}

    # parse the data
    for line in read_data:
        [age, score] = map(int, line.strip().split(" ") )
        # print age, 

        # flatten the age average over X days
        # odd value
        X = 201
        spread = [x-100 for x in range(X)]
        # ages to update
        ages = [age+x for x in spread]
        # remove negative values
        ages = [x for x in ages if x>=0]

        for age in ages:       
            # check if age is a key in dictionary
            if age not in age_dict:
                # create new tuple
                age_dict[age] = [score, 1]
            else:
                # get oldd values
                [old_sum, old_count] = age_dict[age]
                # update values
                age_dict[age] = [old_sum+score, old_count+1]

for age in age_dict:
    [sum_instances, count] = age_dict[age]
    print age, sum_instances/float(count)