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

def draw_n(k,color):
  sumz = 0    
  for i in xrange(0,size,2):
    for j in xrange(0,size,2):
      a = i/512.
      b = j/512.
      val = (k*a+1)**2+(k*b+1)**2
      val = int(val**.5+.5)
      if val == k:
        draw_pt(i,j,color,0)
        sumz+=1
  return sumz/256.**2

r=red = [255,0,0]
g=green =[0,255,0]
b=blue = [0,0,255]
lst = [r,g,b]

sumz = 0
for i in xrange(1,11):
  sumz += draw_n(i,lst[i%3])*i
  print sumz
"""
draw_n(2,green)
draw_n(5,blue)
draw_n(6,red)

draw_n(100,green)
"""

#draw_pt(100,100,[255,0,0],10)
img = smp.toimage( data )       # Create a PIL image
img.show()                      # View in default viewer
