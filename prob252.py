#NOTE TODO need to solve it
import time
import numpy as np
import scipy.misc as smp
from math import *
START = time.time()

S = [290797]
for i in xrange(1000):
    S.append( (S[-1] **2) % 50515093)

T = [ (x %2000) - 1000 for x in S]
points = [ (T[2*x-1], T[2*x]) for x in range(1,501)]


SIZE = 1024
# Create a 512x512x3 array of 8 bit unsigned integers
data = np.zeros( (SIZE,SIZE,3), dtype=np.uint8 )

def draw_pt(x,y,val,r):
  for i in xrange(max(0,x-r),min(x+1+r,SIZE)):
    for j in xrange(max(0,y-r),min(y+1+r,SIZE)):
      data[SIZE-j,i] = val

for i in xrange(0,SIZE):
  data[i,512] = [0,0,255]
  data[512,i] = [0,0,255]

for i in range(len(points)):
    p = points[i]
    x,y = p
    x,y = (x+1000)/2, (y+1000)/2
    draw_pt(x,y, [0,255,0], 1)
    if i <= 20:
        draw_pt(x,y, [255,255,255], 4)

    



img = smp.toimage( data )       # Create a PIL image
img.show()                      # View in default viewer

print "Time Taken:", time.time() - START
