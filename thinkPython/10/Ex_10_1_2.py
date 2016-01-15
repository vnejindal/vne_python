#!/usr/bin/python

def nested_sum(lst_int):
  count = 0
  for i in lst_int:
    if type(i) == int: 
      count += i
    else:
    # vne: tbd: wonder why type(i) == list check does not work in script !
      count += nested_sum(i)
  
  return count

def get_nested_sum():
  """Exercise 1  
     Write a function called nested_sum that takes a nested list of integers and 
     add up the elements from all of the nested lists.
  """
  l_int = [1,2,[], 3,[4,[], 5,[6]],[7],[8,9], 10,[[],11]]
  print 'Sum:', nested_sum(l_int)  
  return

def capitalize_all(t):
  """Takes a list of strings and returns a new list that contains capitalized 
     strings.
  """
  res = []
  for s in t:
    res.append(s.capitalize())
  return res

def capitalize_nested(lst_str):
  """Exercise 2  
    Use capitalize_all to write a function named capitalize_nested that 
    takes a nested list of strings and returns a new nested list with all 
    strings capitalized.
  """
  ret_list = []
  index = 0
  for i in lst_str:
    if type(i) == list:
      ret_list.append(capitalize_nested(lst_str[index]))
    else: 
      ret_list.append(i.capitalize())
    index += 1
  
  return ret_list

def get_capitalize_nested():
  #lst_str = ['abc', ['def',[]], 'mno']
  lst_str = ['abc', ['def'], [[], 'ghi'], [], ['jkl'],'mno']
  print capitalize_nested(lst_str)
  return

def main():
  
  # Ex 10_1
  get_nested_sum()
  # Ex 10_2
  get_capitalize_nested()

if __name__ == '__main__':
    main()