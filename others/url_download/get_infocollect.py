#!/usr/bin/python -tt

# This script downloads the files from urls mentioned in 'infocollect_info.txt' file and stores 
# it into respective directory name

import os
import urllib

def main():
  print "Get infocollect program started"
  input_str = raw_input("Would you like to continue: Y/N")
  print "Received input is", input_str
  
  fobj = open("infocollect_info.txt", "r", 1);
  print "Input File",  fobj.name, "opened"
  
  dwn_dir = "downloads"
  
  if os.path.exists(dwn_dir) != 1 :
    os.mkdir(dwn_dir)
  os.chdir(dwn_dir)
  
  for line in fobj :  
    line.lstrip()
    line.rstrip()
    sub_str = line.split("\t")
    print "Downloading for", sub_str[0], "from", sub_str[1]
    if os.path.exists(sub_str[0]) != 1 :  
      os.mkdir(sub_str[0])
    os.chdir(sub_str[0])
    #Sub-split url to get infocollect file name
    sub_url = sub_str[1].split("name=")
    # Download the file from sub_str[1]
    urllib.urlretrieve(sub_str[1], sub_url[1][:-1])
    os.chdir("../") 
  

  fobj.close()
  
if __name__ == '__main__':
  main()