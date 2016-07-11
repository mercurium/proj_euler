import numpy as np
import scipy.misc as smp
from math import *

size = 1000
RED = [255,0,0]
GREEN = [0,255,0]
BLUE = [0,0,255]
WHITE = [255,255,255]


# Create a 512x512x3 array of 8 bit unsigned integers
data = np.zeros( (size,size,3), dtype=np.uint8 )

def draw_pt(x,y,val,r):
  for i in xrange(max(0,y-r),min(y+1+r,size)):
    for j in xrange(max(0,x-r),min(x+1+r,size)):
      data[i,j] = val
draw_point = draw_pt

def draw_circle():
  for a in range(0,360):
    angle = a/180.*pi
    xpos = 250 + 250 * sin(angle)
    ypos = 500 + 250 * cos(angle)
    if ypos < 0:
      break
    draw_pt(int(xpos),int(ypos),RED,0)


def compute(x):
  total = 0
  for i in xrange(0,100):
    temp = (2**i * x) % 1
    temp = min(temp, (-1*temp)%1)
    total += temp / 2.**i
  return total


def compute_lim(x,lim):
  total = 0
  for i in xrange(lim):
    temp = (2**i * x) % 1
    temp = min(temp, (-1*temp)%1)
    total += temp / 2.**i
  return total


#This draws the blancmange
def draw_blancmange():
  for i in xrange(0,size,1):
    x = i/1000.
    y = compute(x)
    draw_pt(i,size- int(y*size),GREEN,1)


def draw_incr():
  for powz in xrange(10):
    for i in xrange(size):
      x = i/1000.
      y_temp = (2**powz * x) % 1
      y = ( min(y_temp, (-1*y_temp) % 1))
      y /= 2.**powz
      draw_pt(i,size - int(y*size),[0,50 + int(10* powz),0],0)

      comp_y = compute_lim(x,powz)
      draw_pt(i,size - int(size * comp_y), RED,0)

draw_blancmange()
draw_circle()
draw_incr()


#this draws the BLUE line that shows us the middle
for i in xrange(0,size):
  data[i,size/2] = BLUE
  data[size/2,i] = BLUE

cutoff = int(0.0789077879653 * size)
for i in xrange(0,size):
  data[i,cutoff] = WHITE

img = smp.toimage( data )       # Create a PIL image
img.show()                      # View in default viewer


"""
ax^2 + c = 0.01575350519067164x^2 + 120.38735983690111
is my computed formula. It's wrong lololol. But the graph is sooo pretty <3
"""
