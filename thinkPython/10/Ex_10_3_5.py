#!/usr/bin/python

def chop(lst_int):
  """Exercise 5
    Write a function called chop that takes a list, modifies it by removing 
    the first and last elements, and returns None.
  """
  if lst_int == []: return
  del lst_int[0]
  del lst_int[-1]

def middle(lst_int):
  """Exercise 4
    Write a function called middle that takes a list and returns a new list 
    that contains all but the first and last elements. 
    So middle([1,2,3,4]) should return [2,3].
  """
  return lst_int[1:-1]
  

def cumulative_sum(lst_int):
  """Exercise 3
    Write a function that takes a list of numbers and returns the cumulative 
    sum; that is, a new list where the ith element is the sum of the first 
    i+1 elements from the original list. 
    For example, the cumulative sum of [1, 2, 3] is [1, 3, 6].
  """
  ret_list = []
  csum = 0
  for num in lst_int:
    csum += num
    ret_list.append(csum)
  return ret_list

def main():
  list1 = [1,2,3]
  list2 = [1,2,3,4,5,6,7,8,9,0]
  list3 = []  
  
  # Ex 10_3
#  print cumulative_sum(list1)
#  print cumulative_sum(list2)
#  print cumulative_sum(list3)

  # Ex 10_4
#  print middle(list1)
#  print middle(list2)
#  print middle(list3)
  
  # Ex 10_5
  chop(list1)
  print list1
  chop(list2)
  print list2
  chop(list3)
  print list3
  
if __name__ == '__main__':
    main()