#!/usr/bin/python
'''
Exercise 7  
Memoize the Ackermann function from Exercise 5 and see if memoization 
makes it possible to evaluate the function with bigger arguments. 
Hint: no. 

Solution: http://thinkpython.com/code/ackermann_memo.py.
'''

import time
# To hold values of computed ack(m,0)
ack_m_n0 = dict()
# To hold values of ack(m,n) - m,n will be tuples and used
# as key in this dictionary
ack_m_n = dict()



def ack_memo(m,n):
  """
  My implemetation of memoized ack function 
  """
  #print 'ack_memo:', m, n
  if m == 0: 
    return n+1
    #vne:: tbd: we do not need to store this
  if n == 0:
    if m in ack_m_n0: 
      return ack_m_n0[m]
    else: 
      ack_m_n0[m] = ack_memo(m-1,1)
      #print ack_m_n0
      return ack_m_n0[m]
  else:
    t = (m,n)
    if t in ack_m_n: 
      return ack_m_n[t]
    else:
      ack_m_n[t] = ack_memo(m-1,ack_memo(m,n-1))
      #print ack_m_n
      return ack_m_n[t]
    
    #return ack_memo(m-1, ack_memo(m,n-1))
  
def ack(m,n):
  """
  Basic (Non- memoized) implemetation of this function 
  """
#  print m, n
  if m == 0: return n+1
  if n == 0: 
    return ack(m-1,1)
  else:
    return ack(m-1, ack(m,n-1))  

cache = {}
  
def ackermann(m, n):
  """ This is solution from think Python Book:
      Computes the Ackermann function A(m, n)

     See http://en.wikipedia.org/wiki/Ackermann_function
  
      n, m: non-negative integers
  """
  if m == 0:
    return n+1
  if n == 0:
    return ackermann(m-1, 1)
  try:
    return cache[m, n]
  except KeyError:
    cache[m, n] = ackermann(m-1, ackermann(m, n-1))
    return cache[m, n]
   
def main():
  m = 3
  n = 9
  s_t = time.time()
  #print ack(m,n) == 125
  print ack_memo(m,n)  # Maximum it is able to go to 3,9
  print time.time() - s_t
  
if __name__ == '__main__':
  main()

