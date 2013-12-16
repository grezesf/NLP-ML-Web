#!/usr/bin/python
import os
import sys
from bs4 import BeautifulSoup
import datetime
import re

# README
# TASK 2- CLASSIFYING EDITS
# this script extract desired features from the raw data set
# and converts them to WEKA readable .arff format
# input:  data directory
#         desired save location+name
# output: one .arff file       

# main function
def main ():

    # directory containing the raw .html files
    raw_data_dir = os.path.abspath(os.path.normpath(sys.argv[1]))
    print raw_data_dir
    # directory where the results will be saved
    # arff_dir = os.path.dirname(os.path.abspath(os.path.normpath(sys.argv[2])))
    # arff_name = os.path.basename(os.path.abspath(os.path.normpath(sys.argv[2])))
    # hard coded practice arff file - not sure what you wanted here???
    # arff_name = 'practice_arff_file.arff'

    # create the arff file
    # try:
    #     arff_file = open(arff_dir + '/' + arff_name, 'w')
    #     print "created file: ", arff_dir + '/' + arff_name
    # except:
    #     sys.exit("failed to create arff file, exiting")

    # # add headers to arff file
    # arff_file.write("% 1. Title: StackExchange database\n")
    # # arff.write("%% 1. METACRITIC %s database\n" % (arff_filename))

    # arff_file.write("% \n")
    # arff_file.write("%% 2. Created on %s \n" % (datetime.date.strftime(datetime.date.today(), "%Y-%M-%d")) )

    # arff_file.write("@RELATION StackExchange\n\n")

    # when adding a new feature, follow the numbered steps
    # step 1 - add attribute name (ORDER MATTERS!)
    # The <datatype> can be any of the four types currently (version 3.2.1) supported by Weka:
    # numeric
    # <nominal-specification>
    # string
    # date [<date-format>]
    # more at: http://www.cs.waikato.ac.nz/ml/weka/arff.html

    # feature 1: name
    # arff_file.write("@ATTRIBUTE name string\n")

    # # write data line
    # arff_file.write("\n@DATA\n")

    

    # walk the directory for data files
    for (path, dirs, files) in os.walk(raw_data_dir):
        for f in files:
            # work on .html files that are not revisions
            if ".html" in f and "revision" not in f:

                print "\n" + "working on " + path + '/' + f

                # open the file
                with open(path + '/' + f, 'r') as open_f:
                    # make soup
                    f_soup = BeautifulSoup(open_f)

                # reset the values 
                feat_values = []

                # step 2 - extract the feature (KEEP SAME ORDER AS STEP 1)
                # in most cases according to a function defined elsewhere
                # only work on the above soup object (it's the main argument of your function)
                # keep the work done here to a minimum
                # and add it to feat_values
                
                # feature 1: name
                feat = f
                feat_values.append(feat)
                print feat

                # print extract_title(f_soup) + '\n'
                # print extract_question(f_soup) + '\n'
                # print extract_answer(f_soup) + '\n'

            else:
                with open(path + '/' + f, 'r') as open_f:
                    f_soup =  BeautifulSoup(open_f)

                
                extract_revision(f_soup)

                # write the values to the file, not including answer&question media
                # for v in feat_values[:-3]:

                #     if type(v) == unicode:
                #         # if the value is a string (ascii or unicode), add quotation marks for WEKA
                #         arff_file.write('\'' + v.encode('ascii', 'ignore') + '\',')
                #     elif type(v) == str:
                #         arff_file.write('\'' + v + '\',')
                #     else:
                #         # if it's not a string (int etc.), write it as is
                #         arff_file.write(str(v) + ',')

                # # write categories to file without quotes
                # arff_file.write(feat_values[-3] + ',')
                # arff_file.write(feat_values[-2] + ',')

                # # last value has linebreak, not comma
                # if type(feat_values[-1]) == unicode:
                #     arff_file.write('\'' + feat_values[-1].encode('ascii', 'ignore') + '\'\n')
                # else:
                #     arff_file.write(str(feat_values[-1]) + '\n')



                
    # close arff file
    # arff_file.close()

    # return nothing
    return None


# def extract_tags(f_soup):
#     # finds tags
#     tag_list = []
#     tags = f_soup.find_all("div", {"class" : "post-taglist"})
#     for tag in tags:
#         tag_list.append(tag.getText().strip())

#     text = ' '.join(tag_list)
#     # returns list of tags as 1 string

#     # remove non-alphanumeric char
#     text = re.sub(r'[^a-zA-Z0-9]+', ' ', text)
#     return text

def extract_title(f_soup):
    # finds title (aka question title)
    title = f_soup.find_all("div", {"id" : "question-header"})[0].getText().strip()
    text = title

    text = re.sub(r'[^a-zA-Z0-9]+', ' ', text)
    return text


def extract_question(f_soup):
    # finds question 
    question = f_soup.find_all("div", {"class" : "post-text"})[0].getText().strip()
    question_cleaned = ' '.join(question.split())

    text = question_cleaned
    text = re.sub(r'[^a-zA-Z0-9]+', ' ', text)
    return text


def extract_answer(f_soup):
    # finds answers
    answers = f_soup.find_all("div", {"class" : "post-text"})[1:]
    ans_list = []
    for a in answers:
        ans = a.getText().strip()
        ans_cleaned = ' '.join(ans.split())
        ans_list.append(ans_cleaned)
    answers_string = ' '.join(ans_list)

    text = answers_string
    text = re.sub(r'[^a-zA-Z0-9]+', ' ', text)
    return text

def extract_revision(f_soup):
  
    revisions = f_soup.find_all("div", {"class" : "post-text inline-diff"})
    for r in revisions:
        # print r
        revs = r.find_all("span", {"class" : re.compile("diff-")})
        for i in revs:
            print i
        # deletions = r.find("span", {"class" : "diff-delete"})
        # additions = r.find("span", {"class" : "diff-add"})
        # try:
        #     print 'DELETION: ' + deletions.getText()
        #     print 'ADDITION: ' + additions.getText()
        # except:
        #     print 'NONE'
        # deletions = r.find_all("span", {"class" : "diff-delete"})
        # additions = f_soup.find_all("span", {"class" : "diff-add"})
        # print 'DELETIONS:'
        # for d in deletions:
        #     print d.getText().strip()
        # print 'ADDITIONS'
        # for a in additions:
        #     print a.getText().strip()


# Call to main 
if __name__=='__main__':
    main()

