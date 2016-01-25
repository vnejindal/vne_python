#!/usr/bin/python
'''
Exercise 10  
Two words are “rotate pairs” if you can rotate one of them and get the other 
(see rotate_word in Exercise 12).
Write a program that reads a wordlist and finds all the rotate pairs. 
Solution: http://thinkpython.com/code/rotate_pairs.py.
'''


def rotate_pair(w1, w2):
  """ Takes two words w1 and w2 and returns True if they are 'rotate pairs'
  """
  if len(w1) != len(w2): return False
  
  i = 0
  diff = 0
  while i < len(w1):
    if i == 0: 
      diff = ord(w1[i]) - ord(w2[1])
    else:
      if diff != (ord(w1[i]) - ord(w2[i])): return False
  return True
        
def get_word_list(fname):
  """ Reads words from a file and returns a list containing them
  """
  fobj = open(fname)
  count = 0
  if fobj == None:
    print 'Invalid File Name'
    return []
  
  wlist = []
  for line in fobj:
    count += 1
    wlist.append(line.strip().lower())
  
  print count
  return wlist

def get_rotate_pairlist(wlist):
  """ Reads a words list and returns a dictionary with keys & values as 
      rotate pairs
  """
  r_pairs = dict()
  for word in wlist:
    for word2 in wlist:
      if True == rotate_pair(word, word2):
        r_pairs[word] = word2
      wlist.remove(word2)
  
  return r_pairs

def main():
  wlist = get_word_list('words.txt')
  #print get_rotate_pairlist(wlist)
  
if __name__ == '__main__':
  main()
