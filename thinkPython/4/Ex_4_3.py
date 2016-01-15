#!/usr/bin/python
'''
The following sections have solutions to the exercises, so don’t look until 
you have finished (or at least tried).

1. Write a function called square that takes a parameter named t, which 
is a turtle. It should use the turtle to draw a square. 
Write a function call that passes bob as an argument to square, and then 
run the program again.

2. Add another parameter, named length, to square. Modify the body so length 
of the sides is length, and then modify the function call to provide a 
second argument. Run the program again. Test your program with a range of 
values for length.

3. The functions lt and rt make 90-degree turns by default, but you can 
provide a second argument that specifies the number of degrees. 
For example, lt(bob, 45) turns bob 45 degrees to the left.
Make a copy of square and change the name to polygon. Add another parameter 
named n and modify the body so it draws an n-sided regular polygon. 
Hint: The exterior angles of an n-sided regular polygon are 360/n degrees.

4. Write a function called circle that takes a turtle, t, and radius, r, 
as parameters and that draws an approximate circle by invoking polygon with 
an appropriate length and number of sides. Test your function with a 
range of values of r.
Hint: figure out the circumference of the circle and make sure that 
length * n = circumference.
Another hint: if bob is too slow for you, you can speed him up by 
changing bob.delay, which is the time between moves, in seconds. 
bob.delay = 0.01 ought to get him moving.

5. Make a more general version of circle called arc that takes an additional 
parameter angle, which determines what fraction of a circle to draw. 
angle is in units of degrees, so when angle=360, arc should draw a 
complete circle.
'''

import math
from swampy.TurtleWorld import *

def arc(t, radius, angle):
  # nsides * side_len = circumference
  # angle * nsides = 360 (degrees)
  circum = 2 * math.pi * radius 
  n_sides = int(circum/10) + 1  # Approx. calculation of num sides 
  length = circum / n_sides 
  print n_sides , length 
  arc_sides = int (n_sides * ( angle / 360.0))
  polygon(t, length, arc_sides)
  
  # Refer to original solution for better understanding  

def circle(t, radius):

  # nsides * side_len = circumference
  circum = 2 * math.pi * radius 
  n_sides = int(circum/10) + 1  # Approx. calculation of num sides 
  length = circum / n_sides 
  
  print n_sides , length 
  
  polygon(t, length, n_sides)
  
  
def polygon(t, length, nsides):
  
  for i in range(nsides): 
    fd(t,length)
    lt(t, 360/nsides)
    

def square(t, length):
  
  for i in range(4): 
    fd(t,length)
    lt(t)
    

def main():

#  len_str = raw_input('Enter Length: ')
#  nsides = raw_input('Enter number of sides: ')
  
  world = TurtleWorld()
  bob = Turtle()
  bob.delay = 0.01
  print bob
#  square(bob, int(len_str))
#  polygon(bob, int(len_str), int(nsides))
 
#  circle(bob, 50)
  arc(bob, 50, 180)
  wait_for_user()
  
if __name__ == '__main__':
  main()