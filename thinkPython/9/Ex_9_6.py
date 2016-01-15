#!/usr/bin/python

'''
Exercise 6  
Write a function called is_abecedarian that returns True if the letters in a 
word appear in alphabetical order (double letters are ok). How many 
abecedarian words are there?
'''

import string 

def is_abecedarian(word):
  if len(word) <= 1: 
    return True
  
  last_ch = 'a'
  for ch in word:
#    print ord(last_ch), ord(ch)
    if ord(ch) >= ord(last_ch):
#      print last_ch, ch
      last_ch = ch
    else:
      return False
  return True
#vne: Look for other possible implementations using recursion and while look 
# given at: http://www.greenteapress.com/thinkpython/html/thinkpython010.html
#
def words_uses_all(fobj):
  t_count = 0
  ne_count = 0
  
  for word in fobj: 
    t_count += 1    
    if is_abecedarian(word.strip()): print word.strip(); ne_count += 1
        
  
  print "Total Words:", t_count
  print "Words uses all letters:", ne_count 
  print "%age: ", 100* (float(ne_count)/t_count)
  
  
def main():
  fobj = open('words.txt')
  print fobj
  
  words_uses_all(fobj)
  
if __name__ == '__main__':
  main()
  