#!/usr/bin/python

'''
Exercise 3  
Write a function named avoids that takes a word and a string of forbidden 
letters, and that returns True if the word doesn’t use any of the forbidden 
letters.
Modify your program to prompt the user to enter a string of forbidden letters 
and then print the number of words that don’t contain any of them. 
Can you find a combination of 5 forbidden letters that excludes the 
smallest number of words?
'''

import string 

def avoids (word, frbdn_letters):
  """ Returns True if 'word' does not contain any of 'frbdn_letters'
  word: Input word
  frbd_letters:  'String of forbidden letters"
  """
  for letter in frbdn_letters:
    if letter in word: 
      return False
  return True

def words_without_avoids(fobj):
  
  fbdn_letters = 'aeiou' 
  
  t_count = 0
  ne_count = 0
  
  for word in fobj: 
    t_count += 1    
    if avoids(word,fbdn_letters): ne_count += 1
        
  
  print "Total Words:", t_count
  print "Words without forbidden letters:", ne_count 
  print "%age: ", 100* (float(ne_count)/t_count)
  
  
def main():
  fobj = open('words.txt')
  print fobj
  
  words_without_avoids(fobj)
  
if __name__ == '__main__':
  main()
  