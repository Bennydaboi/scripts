import sys
import urllib2

# enter thingspeak API
myAPI = 'ANBQWHHNZ75EZLO2'

# URL where data will be sent
baseURL = 'https://api.thingspeak.com/update?api_key=%s' % myAPI 

# Random value for test
val = 3

# Upload data to thingspeak
conn = urllib2.urlopen(baseURL + '&field1=%s' % (val))
print conn.read()
conn.close()
