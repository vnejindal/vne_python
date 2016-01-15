#!/usr/bin/python

'''
Exercise 4  
Write a function named uses_only that takes a word and a string of letters, 
and that returns True if the word contains only letters in the list. 
Can you make a sentence using only the letters acefhlo? 
Other than “Hoe alfalfa?”
'''

import string 

def uses_only(word, letters):
  
  for letter in word: 
    if letter not in letters: 
      return False
  return True

def words_uses_only(fobj):
  
  fbdn_letters = 'warehousing' 
  
  t_count = 0
  ne_count = 0
  
  for word in fobj: 
    t_count += 1    
    if uses_only(word.strip(),fbdn_letters): ne_count += 1
        
  
  print "Total Words:", t_count
  print "Words uses only letters:", ne_count 
  print "%age: ", 100* (float(ne_count)/t_count)
  
  
def main():
  fobj = open('words.txt')
  print fobj
  
  words_uses_only(fobj)
  
if __name__ == '__main__':
  main()
  