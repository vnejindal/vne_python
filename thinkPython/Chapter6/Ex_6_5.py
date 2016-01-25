#!/usr/bin/python
'''
Exercise 5  

Write a function named ack that evaluates Ackermann’s function. 
Use your function to evaluate ack(3, 4), which should be 125. 
What happens for larger values of m and n? 

Solution: http://thinkpython.com/code/ackermann.py.
'''

import time

def ack(m,n):
  """
  My implemetation of this function 
  """
#  print m, n
  if m == 0: return n+1
  if n == 0: 
    return ack(m-1,1)
  else:
    return ack(m-1, ack(m,n-1))
  
def ackermann(m, n):
  """Computes the Ackermann function A(m, n)
   See http://en.wikipedia.org/wiki/Ackermann_function
   n, m: non-negative integers
  """
  #print 'ackermann:', m,n
  if m == 0:
    return n+1
  if n == 0:
    return ackermann(m-1, 1)
  return ackermann(m-1, ackermann(m, n-1))

def main():
  m = 3
  n = 7
  s_t = time.time()
  #print ack(m,n) == 125 # 3,4
  print ackermann(m,n)
  print time.time() - s_t
  
if __name__ == '__main__':
  main()

