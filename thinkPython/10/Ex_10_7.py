#!/usr/bin/python

'''
Exercise 7  
Two words are anagrams if you can rearrange the letters from one to spell 
the other. 
Write a function called is_anagram that takes two strings and returns True 
if they are anagrams.
'''

def is_anagram(str1, str2):
  if len(str1) != len(str2): return False
  list1 = list(str1)
  list2 = list(str2)
  
  for ch in list1:
    if ch not in list2: return False
    list2.remove(ch)
    
  print list2
  if len(list2) != 0: return False
  return True

def main():
  str1 = 'aabac'
  str2 = 'aacba'
  
  print is_anagram(str1,str2)
    
if __name__ == '__main__':
    main()