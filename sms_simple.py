import urllib2
import json

data = {
            "from":"+1234567",
            "to":"+1234567",
            "body":"Hello world:-)"
 	   }

req = urllib2.Request('http://scsalpha-prod.apigee.net/v1/messaging/sms')
req.add_header('Content-Type', 'application/json; charset=utf-8')
req.add_header('client_id', '%CLIENT_ID%')

result = urllib2.urlopen(req, json.dumps(data))

print '\n'.join(result.readlines())
