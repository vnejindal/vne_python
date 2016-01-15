#!/usr/bin/python


from swampy.TurtleWorld import *

world = TurtleWorld()
bob = Turtle()
print bob

# Draw a right angle 
'''
fd(bob, 100)
lt(bob)
fd(bob, 100)
'''

# Draw a square 
for i in range(4):
  fd(bob,100)
  lt(bob)


wait_for_user()