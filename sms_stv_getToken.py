import urllib2
import json


data = {
           "to":"+1234567"
       }

req = urllib2.Request('https://api.swisscom.com/v1/tokenvalidation')
req.add_header('Content-Type', 'application/json; charset=utf-8')
req.add_header('client_id', '%CLIENT_ID%')

result = urllib2.urlopen(req, json.dumps(data))

print '\n'.join(result.readlines())

