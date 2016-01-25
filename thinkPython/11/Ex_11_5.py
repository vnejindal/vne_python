#!/usr/bin/python

'''
Exercise 5   Read the documentation of the dictionary method setdefault and 
use it to write a more concise version of invert_dict. 
Solution: http://thinkpython.com/code/invert_dict.py.
'''
def solution_histogram(s):
  """ Solution to Exercise 2
  """
  d = dict()
  for c in s:
    d[c] = d.get(c,0) + 1
  return d    

def invert_dict_2(d):
  """ Solution to Exercise 5
  """
  inverse = dict()
  for key in d:
    val = d[key]
    if [key] != inverse.setdefault(val, [key]):
      inverse[val].append(key)
  return inverse


def invert_dict(d):
  inverse = dict()
  for key in d:
    val = d[key]
    if val not in inverse:
      inverse[val] = [key]
    else:
      inverse[val].append(key)
  return inverse


def main():
  
  line = 'This is my program. !'
  
  d = solution_histogram(line)
  print invert_dict(d) 
  print invert_dict_2(d)
  print invert_dict(d) == invert_dict_2(d)
  
if __name__ == '__main__':
  main()
