#!/usr/bin/python


'''
1. Write a function that draws a grid like the following:
+ - - - - + - - - - +
|         |         |
|         |         |
|         |         |
|         |         |
+ - - - - + - - - - +
|         |         |
|         |         |
|         |         |
|         |         |
+ - - - - + - - - - +
Hint: to print more than one value on a line, you can print a comma-separated sequence:
print '+', '-'
If the sequence ends with a comma, Python leaves the line unfinished, so the value printed next appears on the same line.
print '+', 
print '-'
The output of these statements is '+ -'.
A print statement all by itself ends the current line and goes to the next line.

2. Write a function that draws a similar grid with four rows and four columns.

Solution: http://thinkpython.com/code/grid.py. 
'''
def print_pipe():
  print '|', '  '*4, '|','  '*4,'|'

def print_edge_row():
  print '+','- '*4,'+','- '*4,'+'
  
def print_twice(f):
  f()
  f()
  
def print_four(f):
  print_twice(f)
  print_twice(f)

def print_grid():
  print_edge_row()
  print_four(print_pipe)
  print_edge_row()
  print_four(print_pipe)
  print_edge_row()

print_grid()

'''
def main(): 
# print_twice(print_grid)
  print_grid()
  
if __name__ == '__main__':
  main()

Given below is the code copied from standard python script present as 
solution file. This is done for the beauty of that implementation. 
'''

# here is a less-straightforward solution to the
# four-by-four grid
print "Printing 4x4 Grid"

def one_four_one(f, g, h):
    f()
    print_four(g)
#    do_four(g)
    h()

def print_plus():
    print '+',

def print_dash():
    print '-',

def print_bar():
    print '|',

def print_space():
    print ' ',

def print_end():
    print

def nothing():
    "do nothing"

def print1beam():
    one_four_one(nothing, print_dash, print_plus)

def print1post():
    one_four_one(nothing, print_space, print_bar)

def print4beams():
    one_four_one(print_plus, print1beam, print_end)

def print4posts():
    one_four_one(print_bar, print1post, print_end)

def print_row():
    one_four_one(nothing, print4posts, print4beams)

def print_four_grid():
    one_four_one(print4beams, print_row, nothing)

print_four_grid()