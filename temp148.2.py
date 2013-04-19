import numpy as np
import scipy.misc as smp
from math import *

size = 2048
# Create a 512x512x3 array of 8 bit unsigned integers
data = np.zeros( (size//2,size,3), dtype=np.uint8 )


r=red = [255,0,0]
g=green =[0,255,0]
b=blue = [0,0,255]
depth = 1000#size//2 -1
num = 16
     
triangle = [ [1] * (x+1) for x in range(0,depth+1)]
for i in range(1,len(triangle)):
  for j in range(1,len(triangle[i])-1):
    triangle[i][j] = (triangle[i-1][j] + triangle[i-1][j-1]) %num


for i in xrange(0,len(triangle)):
  start_x = size//2 - i
  for j in xrange(0,len(triangle[i])):
    if triangle[i][j]  == 0:
      data[i,start_x] = red
    start_x+=2

for i in xrange(1,int(log(size/2,7)) +1):
  for j in xrange(0,size):
    data[7**i,j] = blue

img = smp.toimage( data )       # Create a PIL image
img.show()                      # View in default viewer
