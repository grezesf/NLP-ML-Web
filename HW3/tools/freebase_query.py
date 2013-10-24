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

# to access Freebase info through its API you need request an API key    
api_key = 'AIzaSyAaPCPkY7cY5sPbM5vprwA-ZsUpdF6mxmY'
service_url = 'https://www.googleapis.com/freebase/v1/mqlread'

# creates new file to write found DOBs 
name_file = open('../data/found_dobs.txt', 'w')

# iterates through list of names, constructs a freebase query, and makes a list of found DOBs for query
# then prints one DOB for each query(if multiple people under same name, DOB picked is the first result, the most common person)
for name in names:
    dob_list = []
    
    # creates freebase query
    print '\nCONSTRUCTING FREEBASE QUERY FOR: %s'%(name)
    query = [{'id': None, 'name': name, 'date_of_birth': None, 'type': '/people/person'}]
    params = {
        'query': json.dumps(query),
        'key': api_key
}
    url = service_url + '?' + urllib.urlencode(params)
    response = json.loads(urllib.urlopen(url).read())
    
    # pulls out the DOB from the returned response
    for person in response['result']:
        string2 = person['date_of_birth']
        print 'DOB:', string2
        # creates list of all DOBs
        dob_list.append(string2)
        
    try:
        # picks first DOB for each query
        best_dob = dob_list[0]
        date = best_dob.split('-')
        # formats DOB to proper form day-month-year and writes it to file
        if len(date) == 1:
            new_dob = '-'.join(['xx','xx',date[0]])
            print new_dob
            name_file.write(new_dob.encode('ascii','ignore')+'\n')
        else:
            new_dob = '-'.join([date[-1], date[1], date[0]])
            print new_dob
            name_file.write(new_dob.encode('ascii','ignore')+'\n')
 
    except:
        # if query can't be found or no DOB exists, print out no DOB
        print 'No DOB for ' + name
        name_file.write('No DOB for ' + name)
        