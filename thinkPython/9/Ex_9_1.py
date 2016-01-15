#!/usr/bin/python

'''
Exercise 1  
Write a program that reads words.txt and prints only the words with more than 
20 characters (not counting whitespace).
'''

def main():
  fobj = open('words.txt')
  print fobj
  
  count = 0
  for word in fobj: 
    if len(word.strip()) > 20: 
      print word
      count += 1
  
  print "Total Words: ", count    
if __name__ == '__main__':
  main()
  