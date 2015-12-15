#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re

summary = False 
summary_file = ''

"""Baby Names exercise

Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

<td>(\d+)</td><td>(\w+)</td><td>(\w+)</td>

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""

def extract_names(filename):
  """
  Given a file name for baby.html, returns a list starting with the year string
  followed by the name-rank strings in alphabetical order.
  ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
  """
  # +++your code here+++
  # Extract year from input filename and add it to return list
  # Now extract each name with rank, create a new string and append 
  # it to another list
  # Sort this one and add the result to final return list 
  
  # Open file name and start reading lines 

  fobj = open(filename, 'r')
  if fobj.closed is not False : 
    print "File %s does not exist"  %(fobj.name())
    sys.exit(0)

  if summary is True : 
    fw_obj = open(summary_file, 'a')
    if fw_obj.closed is not False : 
      print "File %s does not exist"  %(fw_obj.name())
      sys.exit(0)

  name_dict = {}
  year_str = ''	
  for f_line in fobj : 
    # Parse the file to get year  
#    match = re.search(r'Popularity in (\d\d\d\d)', f_line)
    match = re.search(r'Popularity in (\d{4})', f_line)

    if match : 
      #check if this year exists in dictionary, if not add it
      if match.group(1) not in name_dict : 
        name_dict[match.group(1)] = []
        year_str = match.group(1)
    match = re.search(r'<td>(\d+)</td><td>(\w+)</td><td>(\w+)</td>', f_line)
    if match : 
      #print match.group(1), match.group(2), match.group(3)
      str_1 = match.group(2) + ' ' + match.group(1)
      str_2 = match.group(3) + ' ' + match.group(1)
      name_dict[year_str].append(str_1)
      name_dict[year_str].append(str_2)

  fw_obj.write(year_str)
  num_names = 0
  sorted_list = sorted(name_dict[year_str])
  if summary is True :
    for name_str in sorted_list : 
      fw_obj.write(' ' + name_str)
      num_names += 1
  
  fw_obj.write('\n')
  
  print "Written %d entries for year %s" %(num_names, year_str)
  fobj.close()
  if summary is True :
    fw_obj.close()
#vne:: look for solution directory as a different implementation using tuples  
  return

def main():
  # This command-line parsing code is provided.
  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]

  if not args:
    print 'usage: [--summaryfile] file [file ...]'
    sys.exit(1)

  # Notice the summary flag and remove it from args if it is present.
  global summary 
  global summary_file 
  if args[0] == '--summaryfile':
    summary = True
    del args[0]
    summary_file = args[0]
    del args[0]
  # +++your code here+++
  # For each filename, get the names, then either print the text output
  # or write it to a summary file
  for filename in args : 
    extract_names(filename)
#  extract_names(args[0])
  
if __name__ == '__main__':
  main()
