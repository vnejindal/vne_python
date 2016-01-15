#!/usr/bin/python

'''
Exercise 10  
Write a function that reads the file words.txt and builds a list with one 
element per word. Write two versions of this function, one using the append 
method and the other using the idiom t = t + [x]. 
Which one takes longer to run? Why?

Hint: use the time module to measure elapsed time. 
Solution: http://thinkpython.com/code/wordlist.py.
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

def list_add():
  fobj = open('words.txt')
  print fobj
  
  w_list = []
  count = 0
  for word in fobj:
    w_list = w_list + [word.strip()]
    count += 1
  
  print 'Total Words: ',count

def main():
  s_time = time.time()
  list_append()
  print "Append elapsed time", time.time() - s_time
  s_time = time.time()
  list_add()
  print "Add elapsed time", time.time() - s_time
  
if __name__ == '__main__':
  main()

