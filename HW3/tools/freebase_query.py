#!/usr/bin/python
import os
import sys
import json
import urllib

### README
# Takes a list of names as input, creates a freebase query, and returns the date of birth of the query


train_file = sys.argv[1]
train_data = open(train_file, 'r')
names = train_data.readlines()

# To access Freebase info through its API you need request an API key    
api_key = 'AIzaSyAaPCPkY7cY5sPbM5vprwA-ZsUpdF6mxmY'
service_url = 'https://www.googleapis.com/freebase/v1/mqlread'

name_file = open('../data/found_dobs.txt', 'w')
for name in names:
    dob_list = []
    print '\nCONSTRUCTING FREEBASE QUERY FOR: %s'%(name)
    query = [{'id': None, 'name': name, 'date_of_birth': None, 'type': '/people/person'}]
    params = {
        'query': json.dumps(query),
        'key': api_key
}
    url = service_url + '?' + urllib.urlencode(params)
    response = json.loads(urllib.urlopen(url).read())

    for person in response['result']:
        string1 = person['name']
        string2 = person['date_of_birth']
        print 'DOB:', string2
        dob_list.append(string2)
        
    try:
        best_dob = dob_list[0]
        date = best_dob.split('-')
        
        if len(date) == 1:
            new_dob = '-'.join(['xx','xx',date[0]])
            print new_dob
            name_file.write(new_dob.encode('ascii','ignore')+'\n')
        else:
            new_dob = '-'.join([date[-1], date[1], date[0]])
            print new_dob
            name_file.write(new_dob.encode('ascii','ignore')+'\n')
 
    except:
        print 'No DOB for ' + name
        name_file.write('No DOB for ' + name)
        

string1.encode('ascii','ignore')
