#!/usr/bin/python

'''
Exercise 2  
Dictionaries have a method called get that takes a key and a default value. 
If the key appears in the dictionary, get returns the corresponding value; 
otherwise it returns the default value. For example:
>>> h = histogram('a')
>>> print h
{'a': 1}
>>> h.get('a', 0)
1
>>> h.get('b', 0)
0
Use get to write histogram more concisely. 
You should be able to eliminate the if statement.
'''

def histogram(s):
  d = dict()
  for c in s:
    if c not in d:
      d[c] = 1
    else:
      d[c] += 1
  return d

def solution_histogram(s):
  """ Solution to Exercise 2
  """
  d = dict()
  for c in s:
    d[c] = d.get(c,0) + 1
  return d    

def print_hist(h):
  for c in h:
    print c, h[c]

'''
Exercise 3  
Dictionaries have a method called keys that returns the keys of the dictionary, 
in no particular order, as a list.
Modify print_hist to print the keys and their values in alphabetical order.
'''
def print_hist_sort(h):
  t = h.keys()
  t.sort()
  
  for c in t:
    print c, h[c]

def main():
  
  line = 'This is my program !'
  print solution_histogram(line) == histogram(line)
  
  print_hist_sort(solution_histogram(line))

 
if __name__ == '__main__':
  main()

