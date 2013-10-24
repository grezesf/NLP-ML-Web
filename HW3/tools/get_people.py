#!/usr/bin/python
import os
import sys
import json
import urllib

### README
# Used Freebase API to query and access people and DOBS
# Results are 100 names with DOBs

# To query Freebase a API key is required, you must request it
# constructs freebase query, to find list of people and their info (DOB)
api_key = 'AIzaSyAaPCPkY7cY5sPbM5vprwA-ZsUpdF6mxmY'
service_url = 'https://www.googleapis.com/freebase/v1/mqlread'
query = [{'id': None, 'name': None, 'date_of_birth': None, 'type': '/people/person'}]
params = {
        'query': json.dumps(query),
        'key': api_key
}
url = service_url + '?' + urllib.urlencode(params)
response = json.loads(urllib.urlopen(url).read())


# counter = 0
for person in response['result']:
  string1 = person['name']
  string2 = person['date_of_birth']
  print string1.encode('utf-8','ignore'), string2.encode('utf-8','ignore')
  
#   counter += 1
#   print counter
