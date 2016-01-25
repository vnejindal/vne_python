#!/usr/bin/python
'''
Exercise 9  
If you did Exercise 8, you already have a function named has_duplicates that 
takes a list as a parameter and returns True if there is any object that 
appears more than once in the list.
Use a dictionary to write a faster, simpler version of has_duplicates. 

Solution: http://thinkpython.com/code/has_duplicates.py.
'''

def has_duplicates(l):
  dct = dict()  
  for obj in l:
    if obj in dct:
      return True
    else: 
      dct[obj] = 1
  return False

def has_duplicates2(t):
    """Checks whether any element appears more than once in a sequence.

    Faster version using a set.

    t: sequence
    """
    return len(set(t)) < len(t)
  
def main():
  l_list = [1,2,3,'a', 4,5,6]
  
  print has_duplicates(l_list)
  
if __name__ == '__main__':
  main()

