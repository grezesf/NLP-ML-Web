#!/usr/bin/python
import os
import sys
import random
import urllib
from bs4 import BeautifulSoup

### README
# takes 2 text files of lists (site_list and master_list). Processes site_list and randomly walks
# through the links to retrieve question/answer links and edit links. Saves every link visited, saves
# link name to txt file, saves html for Q&A sites, and saves all edit sites html. Data is saved in...


file_list = open('../data/site_list.txt', 'r')
site_list = file_list.readlines()
master_file = open('../data/master_list.txt', 'r+')
master_list = master_file.readlines()

# while loop runs until the site blocks program for making too many requests from the same IP address
stop = 0
while stop == 0:    
    
    # opens site_list.txt and reads list of links    
    # processes each link to topic page to find one question page
    for website in site_list[0:10]:
        numb = random.randrange(0,1000)
        full_link = website.strip() + '/questions/' + str(numb)
        print 'processing link...' + '' + full_link
        if full_link not in master_list:
            print 'Not in master list... then continue'
        
            try:
                # opens question web site
                html = urllib.urlopen(full_link).read()
                # creates beautiful soup object
                soup = BeautifulSoup(html)

                # checks to see if web page is still a valid and active question
                # if it is, it creates a folder for the question page, and creates 2 files (a file with the link and a file with the html)
                # it also creates html files for all the edit pages within the question site

                # if 'Page Not Found' or 'Bad Request' in soup.title.string:
                if 'Bad Request' in soup.title.string or 'Page Not Found' in soup.title.string:
                    print soup.title.string, 'NOT VALID PAGE\n'
                
                # if the site blocks requests, it breaks
                elif 'Too Many Requests' in soup.title.string:
                    print 'TOO MANY REQUESTS!'
                    stop += 1
                    break
                
                # continues if page is valid
                else:
                    
                    # adds valid link to master list and writes it to file
                    print 'VALID PAGE', soup.title.string
                    print 'writing link to master list... ' + full_link 
                    master_file.write(full_link + '\n')
                    master_list.append(full_link)
                    
                    # creates new folder/file name from the link            
                    new_link = full_link.replace('.','_').replace('/','_').replace(':','_')
                    new_path = '../data/' + new_link
                    
                    # creates new folder
                    print 'creating new folder...' + new_path
                    if not os.path.exists(new_path):
                        os.makedirs(new_path)
                
                    # writes link name to txt file
                    link_file = open(new_path + '/' + new_link + '_link.txt', 'w')
                    link_file.write(full_link)
                    print 'wrote link and html to files...' 
                    
                    # writes html to file
                    html_file =  open(new_path + '/' + new_link + '.html','w')
                    html_file.write(html)
             
                    # checks for edit links and writes them their html to files
                    for link in soup.find_all('a'):
                        if 'revisions' in str(link.get('href')):
                            print 'writing edits to files...'
                            edit = str(link.get('href'))
                            edit_link = website.strip() + edit
                            html = urllib.urlopen(edit_link).read()
                            edit_file = open(new_path + '/' + new_link + edit.replace('/','_') + '.html', 'w')
                            edit_file.write(html) 
                    print '\n'

            except:
                print full_link + ' ...NOT VALID LINK\n'   
        else:
            continue
