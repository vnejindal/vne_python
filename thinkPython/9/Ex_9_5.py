#!/usr/bin/python

'''
Exercise 5  
Write a function named uses_all that takes a word and a string of 
required letters, and that returns True if the word uses all the 
required letters at least once. How many words are there that use 
all the vowels aeiou? How about aeiouy?
'''

import string 

def uses_all(word, letters):
  for letter in letters:
    if letter not in word:
      return False
  return True   

def words_uses_all(fobj):
  
  fbdn_letters = 'aeiouy' 
  
  t_count = 0
  ne_count = 0
  
  for word in fobj: 
    t_count += 1    
    if uses_all(word.strip(),fbdn_letters): ne_count += 1
        
  
  print "Total Words:", t_count
  print "Words uses all letters:", ne_count 
  print "%age: ", 100* (float(ne_count)/t_count)
  
  
def main():
  fobj = open('words.txt')
  print fobj
  
  words_uses_all(fobj)
  
if __name__ == '__main__':
  main()
  