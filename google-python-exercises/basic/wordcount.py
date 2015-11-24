#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

"""Wordcount exercise
Google's Python class

The main() below is already defined and complete. It calls print_words()
and print_top() functions which you write.

1. For the --count flag, implement a print_words(filename) function that counts
how often each word appears in the text and prints:
word1 count1
word2 count2
...

Print the above list in order sorted by word (python will sort punctuation to
come before letters -- that's fine). Store all the words as lowercase,
so 'The' and 'the' count as the same word.

2. For the --topcount flag, implement a print_top(filename) which is similar
to print_words() but which prints just the top 20 most common words sorted
so the most common word is first, then the next most common, and so on.

Use str.split() (no arguments) to split on all whitespace.

Workflow: don't build the whole program at once. Get it to an intermediate
milestone and print your data structure and sys.exit(0).
When that's working, try for the next milestone.

Optional: define a helper function to avoid code duplication inside
print_words() and print_top().

"""

import sys

# +++your code here+++
# Define print_words(filename) and print_top(filename) functions.
# You could write a helper utility function that reads a file
# and builds and returns a word/count dict for it.
# Then print_words() and print_top() can just call the utility function.

t_index = 0

def get_next_word(word_str) :
  ret_str = ""
  alpha_flag = 0
  global t_index
  
  l_word_str = word_str[t_index:]
  
  for ctr in l_word_str : 
#    print ctr, ret_str
    t_index += 1
    if ctr.isalpha() :
      ret_str += ctr
      alpha_flag = 1
    else :
      if alpha_flag != 1: 
        ret_str += ctr
      else :
        t_index -= 1	  
      break
    
#  print "returning: ", ret_str, "==>", t_index, l_word_str
  return ret_str	  
	  
def file_open_read(file_name): 

  fobj = open(file_name, "r")

  if fobj.closed == True : 
    print "File %s opening failed. Exiting..." % fobj.name
    sys.exit(0)
  else :
    print "File %s opened in %s format" % (fobj.name, fobj.mode)
  
  file_contents = fobj.read()
  return file_contents

def print_words(filename) : 
  word_dict = {}
  file_contents = file_open_read(filename)
  
#  file_contents.lstrip()
#  file_contents.rstrip()

  lower_file  = file_contents.lower()
  word_list = lower_file
# Split in words  word_list = lower_file.split()
  word_local = get_next_word(word_list)
  while word_local != "" : 
#    print word_local
    word_local = get_next_word(word_list)
    if word_local in word_dict:
      wcount = word_dict[word_local]
      wcount += 1
      word_dict[word_local] = wcount 
    else :
      word_dict[word_local] = 1	
  
  return word_dict

def getCount(dict_tuple):
  return dict_tuple[1]
  
def print_top(filename) : 
  new_list = {}
  word_dict = print_words(filename)
  i = 0
  
  top_items = sorted(word_dict.items(), key=getCount, reverse=True)

  for item in top_items[:20] : print item[0], item[1] 
  return new_list
###

# This basic command line argument parsing code is provided and
# calls the print_words() and print_top() functions which you must define.
def main():
  if len(sys.argv) != 3:
    print 'usage: ./wordcount.py {--count | --topcount} file'
    sys.exit(1)

  option = sys.argv[1]
  filename = sys.argv[2]
  if option == '--count':
    word_dict = print_words(filename)
    for key in sorted(word_dict.keys()): print "%s \t %10d" %( key, word_dict[key] )
  elif option == '--topcount':
    word_dict = print_top(filename)
  else:
    print 'unknown option: ' + option
    sys.exit(1)

if __name__ == '__main__':
  main()
