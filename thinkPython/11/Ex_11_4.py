#!/usr/bin/python

'''
Exercise 4  
Modify reverse_lookup so that it builds and returns a list of all keys 
that map to v, or an empty list if there are none.
'''
def solution_histogram(s):
  """ Solution to Exercise 2
  """
  d = dict()
  for c in s:
    d[c] = d.get(c,0) + 1
  return d    

def reverse_lookup(d, v):
  for k in d:
    if d[k] == v:
      return k
  raise ValueError(d, v)

def reverse_lookup_2(d,v):
  """ Solution to Exercise 4
  """  
  k_list = []
  for k in d:
    if d[k] == v:
      k_list.append(k)
  return k_list

def main():
  
  line = 'This is my program !'
  
  d = solution_histogram(line)
  #print d
  value = 2
  print reverse_lookup (d, value)
  print reverse_lookup_2(d, value)
  
  value = 10
  #print reverse_lookup(d, value)
  print reverse_lookup_2(d, value)
 
if __name__ == '__main__':
  main()
