#!/usr/bin/python


import random

'''
Exercise 9  
Write a function called remove_duplicates that takes a list and returns a 
new list with only the unique elements from the original. 
Hint: they don’t have to be in the same order.
'''
def remove_duplicates(lst):
  tmp_lst = []
  for elem in lst:
    if elem in tmp_lst: pass
    else: tmp_lst.append(elem)
  
  return tmp_lst


'''
Exercise 8  
The (so-called) Birthday Paradox:
1. Write a function called has_duplicates that takes a list and returns True 
if there is any element that appears more than once. It should not modify 
the original list.
2. If there are 23 students in your class, what are the chances that two 
of you have the same birthday? You can estimate this probability by 
generating random samples of 23 birthdays and checking for matches. 
Hint: you can generate random birthdays with the randint function in 
the random module.
You can read about this problem at 
http://en.wikipedia.org/wiki/Birthday_paradox, and you can download my 
solution from http://thinkpython.com/code/birthday.py.
'''
def has_duplicates(lst):
  tmp_lst = []
  for elem in lst:
    if elem in tmp_lst: return True
    else: tmp_lst.append(elem)
  
  return False

def generate_bday_list():
  bday_list = []
  i = 0
  for i in range(23): bday_list.append(random.randint(1,365))
  return bday_list 

def main():
  '''
  list1 = [1,2,3]
  list2 = [1,2,3,4,5,6,7,8,9,0,1]
  
  print has_duplicates(list1)
  print list1
  print has_duplicates(list2)
  print list2
  '''
  i = 0
  count = 0
  tcount = 1000 # No. of iterations
  for i in range(tcount):
    if has_duplicates(generate_bday_list()) == True: count += 1
  
  print "Probability:", 100* float(count)/tcount
    

if __name__ == '__main__':
    main()