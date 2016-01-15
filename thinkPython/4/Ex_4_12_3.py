#!/usr/bin/python

'''
Exercise 3  
Write an appropriately general set of functions that can draw shapes
of regular polygons as in Figure 4.2.
Solution: http://thinkpython.com/code/pie.py.

(Webpage: http://www.greenteapress.com/thinkpython/html/thinkpython005.html)
'''

try: 
  from swampy.TurtleWorld import *
except ImportError: 
  from TurtleWorld import *

import math 


def polyline(t, n, length, angle):
  """Draws n line segments.
  t: Turtle object
  n: number of line segments
  length: length of each segment
  angle: degrees between segments
  """
  for i in range(n):
    fd(t, length)
    lt(t, angle)

def polygon(t, n, length):
  """Draws a polygon with n sides.
  t: Turtle
  n: number of sides
  length: length of each side.
  """
  angle = 360.0/n
  polyline(t, n, length, angle)
  

def draw_pie(t, angle, s_length):
  """Draws a single pie starting with angle 
  t: Turtle
  angle: vertice angle  
  s_length: Length of each side
  """
  # Calculate Length of hypotenuse
  # h_len = (length/2) / (cos(angle/2))
  h_len = (s_length/2) / math.cos(math.radians(angle/2)) 
  
  print h_len, s_length, angle, math.radians(angle/2)

  fd(t, h_len)
  lt(t, 180 - int(angle/2))
  fd(t, s_length)
  lt(t, 180 - int(angle/2))
  fd(t,h_len)
  
def draw_pies(t, nsides, length):
  """Draws a polygon having nsides as set of pies
  t: Turtle
  nsides: number of sides 
  length: length of each side
  """
  vertice_angle = int((nsides - 2)*180/nsides)
  lt(t, int((180 - vertice_angle)/2))
  for i in range(nsides): 
    draw_pie(t,vertice_angle, length)
    lt(t,180)
  

def main():
  world = TurtleWorld()    

  bob = Turtle()
  bob.delay = 0.1
  
  draw_pies(bob, 7 , 50) 
  
if __name__ == '__main__': 
  main()
  
  
