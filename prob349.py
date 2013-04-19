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

graph = [[0]*100 for x in range(100)]

#0 = east, 1 = north, 2 = west
xpos,ypos = 50,50
dirz = 0
for i in xrange(100000):
  if graph[xpos][ypos] == 1:
    graph[xpos][ypos] = 2
    dirz -= 1
  else:
    graph[xpos][ypos] = 1
    dirz += 1
  draw_pt(ypos*5,xpos*5,graph[xpos][ypos]*100,2)
  dirz = dirz%4
  if dirz == 0:
    xpos += 1
  elif dirz == 1:
    ypos += 1
  elif dirz == 2:
    xpos -= 1
  elif dirz == 3:
    ypos -= 1
  if xpos >= 100 or xpos < 0 or ypos >= 100 or ypos < 0:
    break

img = smp.toimage( data )       # Create a PIL image
img.show()                      # View in default viewer



