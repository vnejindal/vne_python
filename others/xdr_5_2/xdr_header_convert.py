#!/usr/bin/python

'''
This script maps PVP xdr file header values into its corresponding text 
present in another file (.mds).
'''


import re

def replace_xdr_file():

  fname = raw_input('Enter the file name: ')

  fname_cds = fname + '.cds'
  fname_mds = fname + '.mds'

  try:
    fobj_cds = open(fname_cds)  
  except:
    print 'File cannot be opened:', fname_cds
    exit()

  try:
    fobj_mds = open(fname_mds)  
  except:
    print 'File cannot be opened:', fname_mds
    exit()
  
# read .mds file as whole 
#  str_mds = fobj_mds.read()
#  print str_mds
  
  # read third line of .cds file
  fobj_cds.readline()
  fobj_cds.readline()
  fline = fobj_cds.readline()

  f_list = fline.split(',')

  try: 
    fobj_op = open("new_xdr.txt","w")
  except:
    print 'Output file cannot be opened'
    exit()  
  
  o_str = ''
  for fld in f_list: 
#    print fld
    fobj_mds.seek(0, 0)  #Offset to 0
    for line_mds in fobj_mds:
      a_line = line_mds.split(',')
      if a_line[0] == fld : 
#        print "Match found", line_mds
        o_str += a_line[1]
        o_str += ','
    
#  print 'Final: ', o_str 
  
  fobj_op.write(o_str)
  
  fobj_cds.close()
  fobj_mds.close()
  fobj_op.close()
  
  return
    
def main():
  replace_xdr_file()

if __name__ == '__main__':
  main()