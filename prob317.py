import numpy as np
import scipy.misc as smp
from math import *

size = 512
# Create a 512x512x3 array of 8 bit unsigned integers
data = np.zeros( (size,size,3), dtype=np.uint8 )

def draw_pt(x,y,val,r):
  for i in xrange(max(0,x-r),min(x+1+r,size)):
    for j in xrange(max(0,y-r),min(y+1+r,size)):
      data[i,j] = val

def calculate_path(angle):
  angle = angle/180.*pi
  for t in xrange(0,400):
    t0 = t/10.
    xpos = 256 + 40 * cos(angle) * t0
    ypos = 200 + 40 * sin(angle) * t0 - 9.81*t0*t0/2
    if ypos < 0:
      break
    draw_pt(int(size -ypos),int(xpos),[255,0,0],0)
      

#This draws the red path that the firecracker splits into
for i in xrange(0,360,1):
  calculate_path(i)

#this draws the blue line that shows us the middle
for i in xrange(0,size):
  data[i,256] = [0,0,255]
  data[256,i] = [0,0,255]

#This draws an approximation to the graph
for t in xrange(-200,200):
  x = 256+t*2
  y = int(229 + t**2/83.)
  draw_pt(y,x,[0,255,0],0)

img = smp.toimage( data )       # Create a PIL image
img.show()                      # View in default viewer


"""
ax^2 + c = 0.01575350519067164x^2 + 120.38735983690111
is my computed formula. It's wrong lololol. But the graph is sooo pretty <3
"""
