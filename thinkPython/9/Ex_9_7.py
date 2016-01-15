#!/usr/bin/python

'''
Exercise 7  
This question is based on a Puzzler that was broadcast on the radio program 
Car Talk (http://www.cartalk.com/content/puzzlers):
Give me a word with three consecutive double letters. I’ll give you a couple 
of words that almost qualify, but don’t. For example, the word committee, 
c-o-m-m-i-t-t-e-e. It would be great except for the ‘i’ that sneaks in there. 
Or Mississippi: M-i-s-s-i-s-s-i-p-p-i. If you could take out those i’s it 
would work. But there is a word that has three consecutive pairs of letters 
and to the best of my knowledge this may be the only word. Of course there 
are probably 500 more but I can only think of one. What is the word?

Write a program to find it. 
Solution: http://thinkpython.com/code/cartalk1.py.
'''

import string 

def is_three_cons(word):
  # Simple straight failure scenario
  if len(word) <= 5: 
    return False
  if (word[0] == word[1]) and (word[2] == word[3]) and (word[4] == word[5]):
    return True
  return False

def is_three_cons_double(word):
  # Simple straight failure scenario
  if len(word) <= 5: 
    return False
  i = 0
  for ch in word: 
  #  print word[i:], i
    if is_three_cons(word[i:]): return True
    i += 1
  
  return False    

def get_all_three_cons_doubles(fobj):
  t_count = 0
  ne_count = 0
  
  for word in fobj: 
    t_count += 1    
    if is_three_cons_double(word.strip()): print word.strip(); ne_count += 1      
  
  print "Total Words:", t_count
  print "Words with 3 consecutive double letters:", ne_count 
  print "%age: ", 100* (float(ne_count)/t_count)
  
  
def main():
  fobj = open('words.txt')
  print fobj
  
  get_all_three_cons_doubles(fobj)
  
if __name__ == '__main__':
  main()
  