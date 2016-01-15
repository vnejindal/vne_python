#!/usr/bin/python

'''
Exercise 11  
To check whether a word is in the word list, you could use the in operator, 
but it would be slow because it searches through the words in order.
Because the words are in alphabetical order, we can speed things up with 
a bisection search (also known as binary search), which is similar to what 
you do when you look a word up in the dictionary. You start in the middle 
and check to see whether the word you are looking for comes before the 
word in the middle of the list. If so, then you search the first half of 
the list the same way. Otherwise you search the second half.

Either way, you cut the remaining search space in half. If the word 
list has 113,809 words, it will take about 17 steps to find the word 
or conclude that it’s not there.

Write a function called bisect that takes a sorted list and a target value 
and returns the index of the value in the list, if it’s there, or 
None if it’s not.

Or you could read the documentation of the bisect module and use that! 
Solution: http://thinkpython.com/code/inlist.py.
'''
import time 

def list_append():
  fobj = open('words.txt')
  print fobj
  
  w_list = []
  count = 0
  for word in fobj:
    w_list.append(word.strip())
    count += 1
  
  print 'Total Words: ',count
  fobj.close()
  
  return w_list 

def dict_list():
  """Uses dictionary for storing the list to make efficient search using 
    in operator
  """
  fobj = open('words.txt')
  print fobj

  count = 0  
  d_list = dict()
  for word in fobj:
    d_list[word.strip()] = 1
    count += 1
  
  print 'Total Words:',count
  fobj.close()
  
  return d_list
  
  
def normal_search(wlist, word):
  """ This word uses in operator for searching 
  """
  return word in wlist

def bisect(wlist, word):
  """Implements binary search for word in wlist
  """
  list_len = len(wlist)
  i = 0 
  while i < list_len:
    i = list_len/2
    if word == wlist[i]:
      return True
    if word < wlist[i]:
      list_len = i
    if word > wlist[i]:
      i += 1

    print i

  return False

def evaluate_time(word):
  """ Evaluates time of different type of searches
  """
  s_time = time.time()
  print normal_search(list_append(), word)
  print "Time taken:", time.time() - s_time
  s_time = time.time()
  print normal_search(dict_list(), word)
  #print word in dict_list()
  print "Dict Time taken:", time.time() - s_time

def main():

  word = 'withstand'
  #print normal_search(list_append(), word)
  #print bisect(list_append(), word)
  evaluate_time(word)
  
if __name__ == '__main__':
  main()

