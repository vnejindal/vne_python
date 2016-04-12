import urllib
import xml.etree.ElementTree as ET

serviceurl = 'http://maps.googleapis.com/maps/api/geocode/xml?'
xml_url = 'http://python-data.dr-chuck.net/comments_42.xml'
xml_url1 = 'http://python-data.dr-chuck.net/comments_216285.xml'

url = urllib.urlopen(xml_url1)
data = url.read()

tree = ET.fromstring(data)
content = tree.findall('.//count')
sum = 0 
for value in content:
  num = value.text
  sum += int(num)

print sum


'''
while True:
    address = raw_input('Enter location: ')
    if len(address) < 1 : break

    url = serviceurl + urllib.urlencode({'sensor':'false', 'address': address})
    print 'Retrieving', url
    uh = urllib.urlopen(url)
    data = uh.read()
    print 'Retrieved',len(data),'characters'
    print data
    tree = ET.fromstring(data)


    results = tree.findall('result')
    lat = results[0].find('geometry').find('location').find('lat').text
    lng = results[0].find('geometry').find('location').find('lng').text
    location = results[0].find('formatted_address').text

    print 'lat',lat,'lng',lng
    print location
'''