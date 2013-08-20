import numpy as np
import scipy.misc as smp
from math import *

size = 1024
block_size = 5
xpos = ypos = size/block_size/2



# Create a 512x512x3 array of 8 bit unsigned integers
data = np.zeros( (size,size,3), dtype=np.uint8 )

def draw_pt(x,y,val,r):
	for i in xrange(max(0,x-r),min(x+1+r,size)):
		for j in xrange(max(0,y-r),min(y+1+r,size)):
			data[i,j] = val

graph = [[0]*(size/block_size) for x in range(size/block_size)]

#0 = east, 1 = north, 2 = west
dirz = 0
for i in xrange(100000):
	if graph[xpos][ypos] == 1:
		graph[xpos][ypos] = 2
		dirz += 1
	else:
		graph[xpos][ypos] = 1
		dirz -= 1
	draw_pt(ypos*block_size,xpos*block_size,graph[xpos][ypos]*100,1)
	dirz = dirz%4
	if dirz == 0:
		xpos += 1
	elif dirz == 1:
		ypos += 1
	elif dirz == 2:
		xpos -= 1
	elif dirz == 3:
		ypos -= 1
	if xpos >= len(graph) or xpos < 0 or ypos >= len(graph) or ypos < 0:
		print "exited the graph at:", i
		break

black_count = 0
for row in graph:
	for item in row:
		if item == 1:
			black_count +=1

print "There were:", black_count, "black squares"

img = smp.toimage( data )			 # Create a PIL image
img.show()											# View in default viewer



