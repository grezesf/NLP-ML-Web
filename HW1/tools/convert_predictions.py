#!/usr/bin/python
import os
import sys
import re


### README
# this script takes as input a Weka style prediction file
# ex: inst#     actual  predicted error distribution ()
#         1     2:GAME     2:GAME       0.333,*0.5,0.167,0 
# and the corresponding arff file
# and outputs a file with predictions as in the homework
# ex: http:__www.metacritic.com_game_pc_alien-rage;GAME;GAME,+

# it also prints the accuracy for nominal classes
# for numeric classes, it only creates a file


# this script is only meant to be called by run_exp.sh
# and never manually 
# for debug only: python ./tools/convert_predictions.py ./results/2013-Oct-10\:38\:37/MEDIA/rep--bag-of-words/MEDIA-rep--bag-of-words.predictions ./data/test/test-feats.arff


# predictions file
pred_file_path = sys.argv[1]
# print pred_file_path

# results directory
work_dir = os.path.dirname(pred_file_path)
# print work_dir

# open the corresponding feats.arff
arff_path = sys.argv[2]
# print arff_path
arff_file = open(arff_path,'r')

#list all the webpages in arff_file
arff_list = re.findall(r"\'www\.metacritic\.com_.*\'," ,arff_file.read())
# print len(arff_list)

# close arff file
arff_file.close()

# open the Weka style predictions file
weka_pred_file = open (pred_file_path, 'r')

if "SCORE" in pred_file_path or "NUMRATINGS" in pred_file_path:
    weka_list= re.findall(r" +\d{1,3} +\d{1,4} +-?\d{1,4}.\d{0,3}", weka_pred_file.read())
    temp = []
    for e in weka_list:
        temp.append(e.split()[1:])
    weka_list = temp
    # print weka_list
else:
    # list all the predictions
    all_labels = re.compile(r" + \d+ +\d:(GAME|TV|MOVIE|MUSIC|GOOD|AVERAGE|BAD|OLD|NEW) +\d:(GAME|TV|MOVIE|MUSIC|GOOD|AVERAGE|BAD|OLD|NEW)")
    weka_list = re.findall(all_labels , weka_pred_file.read())
    # print len(weka_list)

if len(arff_list) != len(weka_list):
    print len(arff_list) , len(weka_list)
    print "Error, weka list does not match the arff file"
    sys.exit()


# create and open new prediction file
new_pred_file = open(work_dir + '/HW1-style--' + os.path.basename(pred_file_path), 'w+')

# inittialize counters for accuracy
good_cnt = 0
bad_cnt = 0

# go through the arff list
for (webpage,pred) in [(arff_list[x], weka_list[x]) for x in range(len(weka_list))]:
    # line to write
    # add webpage
    line = webpage.translate(None, ',\'') + ','
    # add label and prediction
    line += pred[0] + ',' + pred[1] + ','
    
    # add error
    if "SCORE" in pred_file_path or "NUMRATINGS" in pred_file_path:
        line += str(float(pred[1]) - float(pred[0]))
    else:
        # add correct or not
        if pred[0] == pred[1]:
            line += '+'
            good_cnt += 1
        else:
            line += '-'
            bad_cnt += 1
    line += '\n'

    # write line to file
    new_pred_file.write(line)

# print accuracy
if "SCORE" in pred_file_path or "NUMRATINGS" in pred_file_path:
    pass
else:
    print "accuracy: ", (100.0 * good_cnt)/(good_cnt+bad_cnt), "%"
