

import urllib
import json 

serviceurl = 'http://python-data.dr-chuck.net/comments_42.json'
serviceurl = 'http://python-data.dr-chuck.net/comments_216289.json'


uh = urllib.urlopen(serviceurl)
data = uh.read()

info = json.loads(str(data))

sum = 0

if 'comments' not in info:
    print "comments not present"
else:
    for item in info['comments']:
        sum += item['count']

print sum