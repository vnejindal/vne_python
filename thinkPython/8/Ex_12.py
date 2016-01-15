#!/usr/bin/python

'''
Exercise 12  
ROT13 is a weak form of encryption that involves “rotating” each letter in a 
word by 13 places. To rotate a letter means to shift it through the alphabet, 
wrapping around to the beginning if necessary, so ’A’ shifted by 3 is ’D’ 
and ’Z’ shifted by 1 is ’A’.
Write a function called rotate_word that takes a string and an integer as 
parameters, and that returns a new string that contains the letters from the 
original string “rotated” by the given amount.

For example, “cheer” rotated by 7 is “jolly” and “melon” rotated by -10 
is “cubed”.

You might want to use the built-in functions ord, which converts a character 
to a numeric code, and chr, which converts numeric codes to characters.

Potentially offensive jokes on the Internet are sometimes encoded in ROT13. 
If you are not easily offended, find and decode some of them. 

Solution: http://thinkpython.com/code/rotate.py.
'''
def rot13(txt, offset):

  if offset == 0:
    print txt
    return 
  
  for ch in txt: 
    dec = ord(ch)
# check if this letter is a alphabet of not
    if dec >= ord('a') and dec <= ord('z'):
      dec = dec + offset
      if offset > 0 and dec > ord('z'):
        dec = ord('a') + (dec - ord('z'))
      elif offset < 0 and dec < ord('a'):
#        print dec - ord('a')
        dec = ord('z') - (ord('a') - dec -1)
#        print dec, ord('z'), ord('a')
      print chr(dec),       
    elif dec >= ord('A') and dec <= ord('Z'):
      dec = dec + offset
      if offset > 0 and dec > ord('Z'):
        dec = ord('A') + (dec - ord('Z'))
      elif offset < 0 and dec < ord('A'):
        dec = ord('Z') - (ord('A') - dec -1)
      print chr(dec),
    else:
      print ch, 
      
      
def main():
  txt = raw_input("Enter the text: ")
  if len(txt) <= 0:
    exit()
  offset = -10
  rot13(txt, offset)
 

if __name__ == '__main__':
  main()
  