import json
import requests
import urllib2

s = open(".secret").read()
data = json.loads(s)
data['grant_type'] = 'client_credentials'
token = data['access_token']

# acc = requests.post('https://api.yelp.com/oauth2/token', data=data)
# acc_d = acc.json()
# token = acc_d['access_token']

API_URL = 'https://api.yelp.com/v3/businesses/search'
query = "?location=TriBeCa&term=mariachis"

req = urllib2.Request(API_URL + query)
req.add_header('Authorization', 'Bearer ' + token)
resp = urllib2.urlopen(req)
d = json.loads(resp.read())
bs = d['businesses']
for b in bs:
    print b['id']
