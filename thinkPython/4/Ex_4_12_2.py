#!/usr/bin/python

'''
Write an appropriately general set of functions that can draw flowers 
as in Figure 4.1. 
(Webpage: http://www.greenteapress.com/thinkpython/html/thinkpython005.html)

Solution: http://thinkpython.com/code/flower.py, also 
requires http://thinkpython.com/code/polygon.py.
'''

try: 
  from swampy.TurtleWorld import *
except ImportError: 
  from TurtleWorld import *

# import polygon module as well 
#from polygon import *
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

def arc(t, r, angle):
  """Draws an arc with the given radius and angle.
  t: Turtle
  r: radius
  angle: angle subtended by the arc, in degrees
  """
  arc_length = 2 * math.pi * r * abs(angle) / 360
  n = int(arc_length / 4) + 1
  step_length = arc_length / n
  step_angle = float(angle) / n

  # making a slight left turn before starting reduces
  # the error caused by the linear approximation of the arc
  lt(t, step_angle/2)
  polyline(t, n, step_length, step_angle)
  rt(t, step_angle/2)

def circle(t, r):
  """Draws a circle with the given radius.
  t: Turtle
  r: radius
  """
  arc(t, r, 360)

def draw_leaf(t):
  radius = 100
  angle = 60
   
'''  
  pu(t)
  fd(t, radius)
  pd(t)
  lt(t, 135)  
  arc(t, radius, angle)
'''

def draw_circles(t, n_leaves):
  """ Draws n_leaves circles starting from a single point
  t: Turtle
  n_leaves: positive number 
  """
  angle = 0 
  for i in range(n_leaves):
    lt(t, angle)
#    print "LT ", angle, i
    circle(t, 100)
    lt(t, 360 - angle)
    # 1 is added to take care of fractional degree loss
    angle += (int(360/n_leaves) + 1) 
 
def main():
  world = TurtleWorld()    

  bob = Turtle()
  bob.delay = 0.0001  

  draw_circles(bob, 32)
   
if __name__ == '__main__': 
  main()
  
  
