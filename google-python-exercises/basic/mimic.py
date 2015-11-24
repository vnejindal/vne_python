#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

"""Mimic pyquick exercise -- optional extra exercise.
Google's Python Class

Read in the file specified on the command line.
Do a simple split() on whitespace to obtain all the words in the file.
Rather than read the file line by line, it's easier to read
it into one giant string and split it once.

Build a "mimic" dict that maps each word that appears in the file
to a list of all the words that immediately follow that word in the file.
The list of words can be be in any order and should include
duplicates. So for example the key "and" might have the list
["then", "best", "then", "after", ...] listing
all the words which came after "and" in the text.
We'll say that the empty string is what comes before
the first word in the file.

With the mimic dict, it's fairly easy to emit random
text that mimics the original. Print a word, then look
up what words might come next and pick one at random as
the next work.
Use the empty string as the first word to prime things.
If we ever get stuck with a word that is not in the dict,
go back to the empty string to keep things moving.

Note: the standard python module 'random' includes a
random.choice(list) method which picks a random element
from a non-empty list.

For fun, feed your program to itself as input.
Could work on getting it to put in linebreaks around 70
columns, so the output looks better.

"""

import random
import sys

def file_open_read(file_name): 

  fobj = open(file_name, "r")

  if fobj.closed == True : 
    print "File %s opening failed. Exiting..." % fobj.name
    sys.exit(0)
  else :
    print "File %s opened in %s format" % (fobj.name, fobj.mode)
  
  file_content = fobj.read()
  return file_content

def mimic_dict(filename): 
  """Returns mimic dict mapping each word to list of words which follow it."""
  # +++your code here+++
  file_content = file_open_read(filename)
  # Split it by whitespaces
  word_list = file_content.split(None)

  word_dict = {}
  word_dict[''] = []  #Add empty list for empty string
  last_word = ''
  for s_word in word_list : 
    if s_word not in word_dict : 
      word_dict[s_word] = []
    word_dict[last_word].append(s_word)
    last_word = s_word
  
#  print word_dict.items()
  return word_dict
  
# This is another implementation of creating dictionary map  
def mimic_dict_using_nested_lists(filename):
  """Returns mimic dict mapping each word to list of words which follow it."""
  # +++your code here+++
  file_content = file_open_read(filename)
  # Split it by whitespaces
  word_list = file_content.split(None)
 	
  dict_dict = []  # List of unique words occuring in the input file
  final_list = [] # This will hold the list of words following for word present in dict_dict
  
  last_word = ""
  dict_index = 0  # Index to store the unique word in dict_dict 
  final_list.append([])
  dict_dict.append("")
  
  for s_word in word_list : 
#    print last_word, s_word
    # Check if s_word exists in dict_dict, if not add it
    if s_word not in dict_dict : 
      dict_dict.append(s_word)
      final_list.append([])
      dict_index += 1
	# Map s_word with last_word
    final_list[dict_dict.index(last_word)].append(s_word)
#    print s_word, "-->", last_word, len(final_list[dict_dict.index(last_word)])
    last_word = s_word	

  #Print the dictionary now 
  print "Total number of unique words: ", dict_index
  for s_word in dict_dict : 
    print s_word, ":", final_list[dict_dict.index(s_word)]
#    print s_word , len(final_list[dict_dict.index(s_word)])
#    for l_word in final_list[dict_dict.index(s_word)] : 
#      print l_word
	
  return final_list


def print_mimic(mimic_dict, word):
  """Given mimic dict and start word, prints 200 random words."""
  # +++your code here+++
#  print mimic_dict
  
  n_words = 0
  for n_words in range(200) :
    rand_word = random.choice(mimic_dict[word])
    print rand_word,
    word = rand_word
    if len(mimic_dict[word]) == 0 : word = ''  #If it points to empty list, start again with empty string
     
  return


# Provided main(), calls mimic_dict() and mimic()
def main():
  if len(sys.argv) != 2:
    print 'usage: ./mimic.py file-to-read'
    sys.exit(1)

  dict = mimic_dict(sys.argv[1])
  print_mimic(dict, '')


if __name__ == '__main__':
  main()
