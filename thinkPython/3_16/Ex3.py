#!/usr/bin/python

'''
Python provides a built-in function called len that returns the length of a 
string, so the value of len('allen') is 5.
Write a function named right_justify that takes a string named s as a parameter
and prints the string with enough leading spaces so that the last letter of the 
string is in column 70 of the display.
'''

def right_justify(ip_str):
  print 'Adding %d space characters' %(70-len(ip_str))  
  print ' '*(70-len(ip_str)) + ip_str
  return
             

def main():

  ip_str = raw_input('Enter the String: ')
  if len(ip_str) > 70: 
    print "Length greater than 70. Exiting"
    return
    
  right_justify(ip_str) 
  
if __name__ == '__main__':
  main()