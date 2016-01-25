#!/usr/bin/python

'''
Exercise 6  
Run this version of fibonacci and the original with a range of parameters and 
compare their run times.

VNE:: It additionally computes number of computations happening in both 
versions. This can be extended to store the computations in the list and 
then compare how they increase and can be plotted as well. 
'''

import time

known = {0:0, 1:1}
add_count = 0 # for old fibonacci function
madd_count = 0 # for memo based fibonacci function 

def memo_fibonacci(n):
  if n in known:
    return known[n]

  res = memo_fibonacci(n-1) + memo_fibonacci(n-2)
  global madd_count 
  madd_count += 1
  known[n] = res
  return res

def fibonacci(n):
  if n == 0:
    return 0
  elif  n == 1:
    return 1
  else:
    global add_count 
    add_count += 1
    return fibonacci(n-1) + fibonacci(n-2)

def main():
  
  value = 30 # Interesting to see how time increases with increase in the value
  
  s_t = time.time()
  fibonacci(value)
  print time.time() - s_t
  print 'Computations:', add_count
  
  s_t = time.time()
  memo_fibonacci(value)
  print time.time() - s_t
  print 'Computations:', madd_count
  
if __name__ == '__main__':
  main()
