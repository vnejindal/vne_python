
#!/usr/bin/python

'''
Data Format: 
<tr><td>Modu</td><td><span class="comments">90</span></td></tr>
<tr><td>Kenzie</td><td><span class="comments">88</span></td></tr>
<tr><td>Hubert</td><td><span class="comments">87</span></td></tr>
'''

import urllib
from BeautifulSoup import *
 
def count_num_in_html():
  # url = raw_input('Enter - ')
  url = 'http://python-data.dr-chuck.net/comments_42.html'
  url = 'http://python-data.dr-chuck.net/comments_216288.html'
  
  html = urllib.urlopen(url).read()
  soup = BeautifulSoup(html)
  
  # Retrieve all of the anchor tags
  tags = soup('span')
  count = 0
  for tag in tags:
    value = tag.contents[0]
    count += int(value)
    # Look at the parts of a tag
    #print 'TAG:',tag
    #print 'URL:',tag.get('href', None)
    #print 'Contents:',tag.contents[0]
    #print 'Attrs:',tag.attrs  
  print count
  
def main():
  count_num_in_html()
 
if __name__ == '__main__':
  main()