#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil
import commands
import subprocess

"""Copy Special exercise
  The copyspecial.py program takes one or more directories as its arguments. 
  We'll say that a "special" file is one where the name contains the pattern __w__ somewhere, 
  where the w is one or more word chars. The provided main() includes code to parse the 
  command line arguments, but the rest is up to you. Write functions to implement the 
  features below and modify main() to call your functions.

  Suggested functions for your solution(details below):

  get_special_paths(dir) -- returns a list of the absolute paths of the special files in the given directory
  copy_to(paths, dir) given a list of paths, copies those files into the given directory
  zip_to(paths, zippath) given a list of paths, zip those files up into the given zipfile
"""

# +++your code here+++
# Write functions and modify main() to call them
# get_special_paths(dir) -- 
#    returns a list of the absolute paths of the special files in the given directory

def get_special_paths(dir): 
  print "Listing files in", dir
  sp_file_list = []
  files = os.listdir(dir)
  for filename in files: 
    #print filename
    match = re.search(r'.*__\w+__.*',filename)
    if match :
      #print os.path.join(dir,match.group())
      #print os.path.abspath(os.path.join(dir,match.group()))
      sp_file_list.append(os.path.abspath(os.path.join(dir,match.group())))
  
  return sp_file_list

# copy_to(paths, dir) - 
#     given a list of paths, copies those files into the given directory
def copy_to(paths, dir):
  count = 0
  # Check if 'dir' exists
  if not os.path.exists(dir) : 
    os.mkdir(dir) 
	
  for path in paths: 
    shutil.copy(path, dir)
    count += 1
  print count, "files copied"
  return   
#   zip_to(paths, zippath) - 
#        given a list of paths, zip those files up into the given zipfile
def zip_to(paths, zippath): 

  if os.path.exists(zippath): 
    os.rmdir(zippath)
  cmd_line = 'tar -cvf ' + zippath + ' ' + ' '.join(paths)

  print cmd_line	
  # using subprocess module instead  
  subprocess.call(cmd_line)
  return 

'''
  (status, output) = commands.getstatusoutput(cmd_line)
  if status: 
    print "Error" 
    sys.stderr.write(output)
    sys.exit(1)
  print "Success:", status, output 
'''
  
def main():
  # This basic command line argument parsing code is provided.
  # Add code to call your functions below.

  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]
  if not args:
    print "usage: [--todir dir][--tozip zipfile] dir [dir ...]";
    sys.exit(1)

  # todir and tozip are either set from command line
  # or left as the empty string.
  # The args array is left just containing the dirs.
  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]
	
  tozip = ''
  if args[0] == '--tozip':
    tozip = args[1]
    del args[0:2]

  if len(args) == 0:
    print "error: must specify one or more dirs"
    sys.exit(1)

  # +++your code here+++
  # Call your functions
  # vne:: tbd dirs parsing 
  if todir is not '' : 
    sp_file_list = get_special_paths(args[0])
    copy_to(sp_file_list, todir)

  if tozip is not '' : 
    sp_file_list = get_special_paths(args[0])
    zip_to(sp_file_list, tozip)

  #sp_file_list = get_special_paths(args[0])
  
if __name__ == "__main__":
  main()
