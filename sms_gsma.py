import urllib2
import json

data = {
    	'outboundSMSMessageRequest': {
    	'address':['tel:+1234567'],
 		'senderAddress':'tel:+1234567',
 		'outboundSMSTextMessage': {
   		    'message':'Hello world :-)'
    	    }
 		}
 	}

req = urllib2.Request('https://api.swisscom.com/v1/messaging/sms/outbound/tel%3A%1234567/requests')
req.add_header('Content-Type', 'application/json; charset=utf-8')
req.add_header('client_id', '%CLIENT_ID%')

result = urllib2.urlopen(req, json.dumps(data))

print '\n'.join(result.readlines())
