#!/usr/bin/python

import urllib
from BeautifulSoup import *

def follow_href():
  #url = raw_input('Enter URL - ')
  url = 'http://python-data.dr-chuck.net/known_by_Fikret.html'
  url = 'http://python-data.dr-chuck.net/known_by_Conghaile.html'
  count = raw_input('Enter count - ')
  position = raw_input('Enter position - ')
  
  count = int(count)
  
  while (count != 0):
    print 'Reading from url: ', url
    pos = int(position)
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html)
    
    count -= 1
    # Retrieve all of the anchor tags
    tags = soup('a')
    for tag in tags:
      nurl = tag.get('href', None)
      pos -= 1
      if (pos == 0):
        url = nurl 
        break
    
  print url
  
def main():
  follow_href()
 
if __name__ == '__main__':
  main()