#!/usr/bin/python

'''
Exercise 8   
Here’s another Car Talk Puzzler (http://www.cartalk.com/content/puzzlers):
“I was driving on the highway the other day and I happened to notice my 
odometer. Like most odometers, it shows six digits, in whole miles only. 
So, if my car had 300,000 miles, for example, I’d see 3-0-0-0-0-0.
“Now, what I saw that day was very interesting. I noticed that the last 
4 digits were palindromic; that is, they read the same forward as backward. 
For example, 5-4-4-5 is a palindrome, so my odometer could have read 
3-1-5-4-4-5.
“One mile later, the last 5 numbers were palindromic. For example, it 
could have read 3-6-5-4-5-6. One mile after that, the middle 4 out of 
6 numbers were palindromic. And you ready for this? One mile later, 
all 6 were palindromic!

“The question is, what was on the odometer when I first looked?”

Write a Python program that tests all the six-digit numbers and prints 
any numbers that satisfy these requirements. 
Solution: http://thinkpython.com/code/cartalk2.py.

'''

import string 

def is_reverse(word1, word2):
  """Returns True if word2 is reverse of word1. 
  word1: Input Word 1
  word2: Input Word 2
  returns: True/False
  """
  return (word1[::1] == word2[::-1])

def is_palindrome(word):
  """Returns True if word is a palindrome
  """
  return is_reverse(word, word)

def check_cond1(number):
  return is_palindrome(str(number)[-4:])
def check_cond2(number):
  return is_palindrome(str(number)[-5:])
def check_cond3(number):
  return is_palindrome(str(number)[1:5])
def check_cond4(number):
  return is_palindrome(str(number))

def get_number():
  i = 100000
  while i < 999996:  #Important: Traverse till this value to avoid overflow
    if check_cond1(i):
      if check_cond2(i+1):
        if check_cond3(i+2):
          if check_cond4(i+4):
            print 'Number:', i
            #break
    i += 1

def main():
  get_number()
  
if __name__ == '__main__':
  main()
  