import string, time
import numpy as np
import scipy.misc as smp
from math import *
START = time.time()

size = 1024
# Create a 512x512x3 array of 8 bit unsigned integers
data = np.zeros( (size,size,3), dtype=np.uint8 )
RED = [255,0,0]

def draw_pt(x,y,val,r):
    for i in xrange(max(0,x-r),min(x+1+r,size)):
        for j in xrange(max(0,y-r),min(y+1+r,size)):
            data[i,j] = val

def draw_line(x0,y0, direct):
    if direct %4 == 0:
        x1,y1 = x0+1,y0
    elif direct %4 == 1:
        x1,y1 = x0,y0+1
    elif direct %4 == 2:
        x1,y1 = x0-1,y0
    else:
        x1,y1 = x0, y0-1
    draw_pt(x0,y0,RED,0)

    

a = 'aRbFR'
b = 'LFaLb'

start = 'Fa'
endplaces = []

for i in xrange(18):
    start_array = list(start)
    for j in xrange(len(start_array)):
        if start_array[j] == 'a':
                start_array[j] = a
        if start_array[j] == 'b':
                start_array[j] = b
    start = string.join(start_array,'')
    print len(start)
    endplaces.append(len(start))

x,y = 200,600
direction = 1
argablargh = 1
for count in xrange(len(start)):
    c = start[count]
    if count in endplaces:
        print argablargh, x-200,y-600
        argablargh+=1
    if c == 'a' or c == 'b':
        continue
    if c == 'L':
        direction +=1
    elif c == 'R':
        direction -=1
    else:
        draw_line(x,y,direction)
        x += 1*((direction+1) %2)* (-1)**(direction/2)
        y += 1*(direction%2)* (-1)**(direction/2)
        x,y = int(x),int(y)
print x-200,y-600

img = smp.toimage( data )       # Create a PIL image
img.show()                      # View in default viewer
"""
xy = [1,1]
for i in xrange(50):
    xy[0], xy[1] = xy[0]+xy[1], xy[1] - xy[0]
    print i+1, xy
"""
print "Time Taken:", time.time() - START 

