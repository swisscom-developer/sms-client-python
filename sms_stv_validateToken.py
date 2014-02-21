import urllib2
import sys

req = urllib2.Request('https://api.swisscom.com/v1/tokenvalidation/%1234567/%CODE%')
req.add_header('client_id', '%CLIENT_ID%')

result = urllib2.urlopen(req)

print 'StatusHTTP ' + str(result.code) + ' OK'

