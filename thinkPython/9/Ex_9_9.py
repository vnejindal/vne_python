#!/usr/bin/python

'''
Exercise 9   
Here’s another Car Talk Puzzler you can solve with a search 
(http://www.cartalk.com/content/puzzlers):
“Recently I had a visit with my mom and we realized that the two digits 
that make up my age when reversed resulted in her age. For example, if 
she’s 73, I’m 37. We wondered how often this has happened over the years 
but we got sidetracked with other topics and we never came up with an answer.
“When I got home I figured out that the digits of our ages have been 
reversible six times so far. I also figured out that if we’re lucky it 
would happen again in a few years, and if we’re really lucky it would 
happen one more time after that. In other words, it would have happened 
8 times over all. So the question is, how old am I now?”

Write a Python program that searches for solutions to this Puzzler. 
Hint: you might find the string method zfill useful.

Solution: http://thinkpython.com/code/cartalk3.py.
'''

import string 

def is_reverse(word1, word2):
  """Returns True if word2 is reverse of word1. 
  word1: Input Word 1
  word2: Input Word 2
  returns: True/False
  """
  return (word1[::1] == word2[::-1])

def compare_ages(c_age, m_age):
  """Compares age of Mother and Daughter and returns True if all of 
    following conditions match:
    -- Age must be between 1-98 years
    -- Daughter must be younger than Mother
    -- Mother must be 15 years younger than Mother (General Assumption)
    -- Mother age is reverse of Daughter Age. 
  c_age: Daughter's Age
  m_age: Mother's Age
  returns: True/False
  """
    
  if c_age <= 0  or c_age >= 99:
    return False
  if m_age <= 0 or m_age >= 99:
    return False
  if c_age >= m_age or m_age - c_age < 15:
    return False
  
  return is_reverse(str(c_age).zfill(2), str(m_age).zfill(2)) 

def main():
  # Range to try: 1 - 99
  rev_count = 0
  i = 0
  for i in range(99):
    c_age = i
    # Find age of mother in reverse 
    k = 0
    for k in range(99):
      if compare_ages(c_age, k): break
    
    m_age = k    
    #print "Starting with", c_age, m_age
    rev_count = 0
    j = 0
    while j < m_age: 
      # Look for 6 occurences in past
      if compare_ages(c_age - j, m_age - j):
        rev_count += 1
        #print "\tReverse Found: ", rev_count, c_age - j, m_age - j, j
      if rev_count == 6: 
        k = 1
        # Check for 2 future occurences
        while k < 99:
          if compare_ages(c_age + k, m_age + k):
            rev_count += 1
            #print "\tREVERSE Found: ", rev_count, c_age + k, m_age + k, k
          if rev_count == 8: 
            print "8 occurences of age", c_age, m_age
            break
          k += 1
      j += 1
    
if __name__ == '__main__':
  main()
  