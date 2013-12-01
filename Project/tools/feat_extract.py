#!/usr/bin/python
import os
import sys
from bs4 import BeautifulSoup
import datetime

# README
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
    arff_dir = os.path.dirname(os.path.abspath(os.path.normpath(sys.argv[2])))
    # arff_name = os.path.basename(os.path.abspath(os.path.normpath(sys.argv[2])))
    arff_name = 'practice_arff_file.arff'

    # create the arff file
    try:
        arff_file = open(arff_dir + '/' + arff_name, 'w')
        print "created file: ", arff_dir + '/' + arff_name
    except:
        sys.exit("failed to create arff file, exiting")

    # add headers to arff file
    arff_file.write("% 1. Title: StackExchange database\n")
    # arff.write("%% 1. METACRITIC %s database\n" % (arff_filename))

    arff_file.write("% \n")
    arff_file.write("%% 2. Created on %s \n" % (datetime.date.strftime(datetime.date.today(), "%Y-%M-%d")) )

    arff_file.write("@RELATION StackExchange\n\n")

    # when adding a new feature, follow the numbered steps
    # step 1 - add attribute name (ORDER MATTERS!)
    # The <datatype> can be any of the four types currently (version 3.2.1) supported by Weka:
    # numeric
    # <nominal-specification>
    # string
    # date [<date-format>]
    # more at: http://www.cs.waikato.ac.nz/ml/weka/arff.html

    # feature 1: name
    arff_file.write("@ATTRIBUTE name string\n")
    # feature 2: score
    arff_file.write("@ATTRIBUTE score numeric\n")

 
    # write data line
    arff_file.write("\n@DATA\n")

    cpt = 0

    # walk the directory for data files
    for (path, dirs, files) in os.walk(raw_data_dir):
        for f in files:
            # work on .html files that are not revisions
            if ".html" in f and "revision" not in f and cpt<5:
                cpt +=1
                print "working on " + path + '/' + f

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

                # feature 2: score
                feat = extract_score(f_soup)
                feat_values.append(feat)


                # write the values to the file
                for v in feat_values[:-1]:
                    if type(v) == str:
                        # if the value is a string, add quotation marks for WEKA
                        arff_file.write('\'' + v + '\',')
                    else:
                        # if it's not a string, write it as is
                        arff_file.write(str(v)+',')
                # last value had linebreak, not comma
                if type(feat_values[-1]) == str:
                    arff_file.write('\'' + type(feat_values[-1]) + '\',')
                else:
                    arff_file.write(str(feat_values[-1]) + '\n')

                print feat_values
    # close arff file
    arff_file.close()

    # return nothing
    return None

def extract_score(f_soup):
    # find score
    # its the first of the vote-count-post
    score = f_soup.find_all("span", {"class":"vote-count-post "})[0].getText()

    return score

# def extract_tags(f_soup):
#     # find tags

# Call to main 
if __name__=='__main__':
    main()


