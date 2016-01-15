#!/usr/bin/python

'''
Exercise 1  
Write a function that reads the words in words.txt and stores them as keys 
in a dictionary. It doesn’t matter what the values are. Then you can use 
the in operator as a fast way to check whether a string is in the dictionary.
If you did Exercise 11, you can compare the speed of this implementation 
with the list in operator and the bisection search.
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

