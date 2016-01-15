#!/usr/bin/python

'''
Exercise 2
In 1939 Ernest Vincent Wright published a 50,000 word novel called Gadsby 
that does not contain the letter “e.” Since “e” is the most common letter 
in English, that’s not easy to do.
In fact, it is difficult to construct a solitary thought without using 
that most common symbol. It is slow going at first, but with caution and 
hours of training you can gradually gain facility.

All right, I’ll stop now.

Write a function called has_no_e that returns True if the given word doesn’t 
have the letter “e” in it.

Modify your program from the previous section to print only the words that 
have no “e” and compute the percentage of the words in the list have no “e.”
'''

import string 

def has_no_e (word):
  """ Returns True if 'e' is present in the word, else False
  word: Input String 
  """
  return 'e' in word
def words_no_e(fobj):
  
  t_count = 0
  ne_count = 0
  
  for word in fobj: 
    t_count += 1    
    if has_no_e(word): ne_count += 1
        
  
  print "Total Words:", t_count
  print "Words with no 'e':", ne_count 
  print "%age: ", 100* (float(ne_count)/t_count)
  
  
def main():
  fobj = open('words.txt')
  print fobj
  
  words_no_e(fobj)
  
if __name__ == '__main__':
  main()
  