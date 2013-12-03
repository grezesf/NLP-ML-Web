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
    # hard coded practice arff file - not sure what you wanted here???
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
    # feature 3: tags
    arff_file.write("@ATTRIBUTE tags string\n")
    # feature 4: title
    arff_file.write("@ATTRIBUTE title string\n")
    # feature 5: question
    arff_file.write("@ATTRIBUTE question string\n")
    # feature 6: answers
    arff_file.write("@ATTRIBUTE answers string\n")
    # feature 7: numberofanswers
    arff_file.write("@ATTRIBUTE numberofanswers numeric\n")
    # feature 8: questionmedia
    arff_file.write("@ATTRIBUTE questionmedia {NONE, CODE, PIC, LINK, CODELINK, CODEPIC, LINKPIC, THREE}\n")
    # feature 9: answermedia
    arff_file.write("@ATTRIBUTE answermedia {NONE, CODE, PIC, LINK, CODELINK, CODEPIC, LINKPIC, THREE}\n")
    # feature 10: favoritecount
    arff_file.write("@ATTRIBUTE favoritecount numeric\n")
    # write data line
    arff_file.write("\n@DATA\n")

    cpt = 0

    # walk the directory for data files
    for (path, dirs, files) in os.walk(raw_data_dir):
        for f in files:
            # work on .html files that are not revisions
            if ".html" in f and "revision" not in f and cpt<6000:
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

                # feature 3: tags
                feat = extract_tags(f_soup)
                feat_values.append(feat)

                # feature 4: title 
                feat = extract_title(f_soup)
                feat_values.append(feat)

                # feature 5: question
                feat = extract_question(f_soup)
                feat_values.append(feat)

                # feature 6: answers
                feat = extract_answer(f_soup)
                feat_values.append(feat)

                # feature 7: number of answers (per question)
                feat = extract_number_answers(f_soup)
                feat_values.append(feat)

                # feature 8: questionmedia
                feat = extract_question_media(f_soup)
                feat_values.append(feat)

                # feature 9: answermedia
                feat = extract_answer_media(f_soup)
                feat_values.append(feat)

                #feature 10: favoritecount
                feat = extract_favcount(f_soup)
                feat_values.append(feat)

                # write the values to the file, not including answer&question media
                for v in feat_values[:-3]:

                    if type(v) == unicode:
                        # if the value is a string (ascii or unicode), add quotation marks for WEKA
                        arff_file.write('\'' + v.encode('ascii', 'ignore') + '\',')
                    elif type(v) == str:
                        arff_file.write('\'' + v + '\',')
                    else:
                        # if it's not a string (int etc.), write it as is
                        arff_file.write(str(v) + ',')

                # write categories to file without quotes
                arff_file.write(feat_values[-3] + ',')
                arff_file.write(feat_values[-2] + ',')

                # last value has linebreak, not comma
                if type(feat_values[-1]) == unicode:
                    arff_file.write('\'' + feat_values[-1].encode('ascii', 'ignore') + '\'\n')
                else:
                    arff_file.write(str(feat_values[-1]) + '\n')



                
    # close arff file
    arff_file.close()

    # return nothing
    return None

def extract_score(f_soup):
    # find score
    # its the first of the vote-count-post
    score = f_soup.find_all("span", {"class":"vote-count-post "})[0].getText()

    return int(score)


def extract_tags(f_soup):
    # finds tags
    tag_list = []
    tags = f_soup.find_all("div", {"class" : "post-taglist"})
    for tag in tags:
        tag_list.append(tag.getText().strip())

    tags_string = ' '.join(tag_list)
    # returns list of tags as 1 string

    return tags_string 

def extract_title(f_soup):
    # finds title (aka question title)
    title = f_soup.find_all("div", {"id" : "question-header"})[0].getText().strip()

    return title


def extract_question(f_soup):
    # finds question 
    question = f_soup.find_all("div", {"class" : "post-text"})[0].getText().strip()
    question_cleaned = ' '.join(question.split())

    return question_cleaned


def extract_answer(f_soup):
    # finds answers
    answers = f_soup.find_all("div", {"class" : "post-text"})[1:]
    ans_list = []
    for a in answers:
        ans = a.getText().strip()
        ans_cleaned = ' '.join(ans.split())
        ans_list.append(ans_cleaned)
    answers_string = ' '.join(ans_list)

    return answers_string


def extract_number_answers(f_soup):
    # counts number of answers
    answers = f_soup.find_all("div", {"class" : "post-text"})
    number_of_answers = len(answers)

    return number_of_answers

def extract_question_media(f_soup):
    # extracts media for question, tells if non-linguistic info (pictures, links, code) is included 
    media = []
    p = f_soup.find_all("div", {"class": 'post-text'})[0]
    pics = p.find_all("img")
    links = p.find_all("a")
    code = p.find_all("pre")

    if code != [] and 'CODE' not in media:
        media.append('CODE')
    elif pics != [] and 'PIC' not in media:
        media.append('PIC')
    elif links != [] and 'LINK' not in media:
        media.append('LINK')

    if media != [] and len(media) != 3:
        ordered_media = sorted(media)
        return ''.join(ordered_media)

    elif len(media) == 3:
        return 'THREE'
    else:
        return 'NONE'

def extract_answer_media(f_soup):
    # extracts media for answers, tells if non-linguistic info (pictures, links, code) is included 
    media = []
    posts = f_soup.find_all("div", {"class": 'post-text'})
    for p in posts[1:]:
        pics = p.find_all("img")
        links = p.find_all("a")
        code = p.find_all("pre")
        if code != [] and 'CODE' not in media:
            media.append('CODE')
        elif pics != [] and 'PIC' not in media:
            media.append('PIC')
        elif links != [] and 'LINK' not in media:
            media.append('LINK')

    if media != [] and len(media) != 3:
        ordered_media = sorted(media)
        return ''.join(ordered_media)
        
    elif len(media) == 3:
        return 'THREE'
    else:
        return 'NONE'

def extract_favcount(f_soup):
    # extracts favorite count (only for questions)
    favorite_count = f_soup.find("div", {"class" : "favoritecount"}).find("b").getText()
    if favorite_count != '':
        return int(favorite_count)
    else:
        return 0


        

# Call to main 
if __name__=='__main__':
    main()


