#!/usr/bin/python

'''
Exercise 6   
Write a function called is_sorted that takes a list as a parameter and 
returns True if the list is sorted in ascending order and False otherwise. 
You can assume (as a precondition) that the elements of the list can be 
compared with the relational operators <, >, etc.
For example, is_sorted([1,2,2]) should return True and 
is_sorted(['b','a']) should return False.
'''

def is_sorted(llist):
  
  if llist == [] : return True
  
  l_num = llist[0]
  for num in llist:
    if num < l_num: return False
    l_num = num
  
  return True


def main():
  list1 = [1,2,3]
  list2 = [1,2,3,4,5,6,7,8,9,0]
  
  list3 = []  
  list4 = [1,2,2]
  list5 = ['c', 'a','b']
  
#  print is_sorted(list1)
#  print is_sorted(list2)
  print is_sorted(list3)
  print is_sorted(list4)
  print is_sorted(list5)
  
if __name__ == '__main__':
    main()