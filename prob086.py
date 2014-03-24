import math
import time
start = time.time()

size = M = 2000
squares = set([x**2 for x in range(size*3)])
count = 0


#O(n^2)... meh. Was going to make it better but .7389 seconds seems good enough
for b in range(1,size+1): 
  for a in range(1,2*b):
    if a**2+b**2 in squares:
      if a < b: 
        #a=4, b= 5 could be 1,3,5 or 2,2,5.
        count += (a)/2 #assuming 3,5,6 != 5,3,6
        #print b,a, (a)/2, 'raaah'
      else:
        #a=8, b=6 could be 2,6,6 or 3,5,6 or 4,4,6.
        count += b+1-(a+1)/2
        #print b,a, b+1-(a+1)/2, 'fu gahhh'
  if count > 10**6:
    print b
    break

print count
print "Time Taken: ", time.time() - start

"""
#this was my dumb method for debugging my math: O(n^3)
count = 0
for i in range(1,size+1):
  for j in range(1,i+1):
    for k in range(1,j+1):
      if (j+k)**2 + i**2 in squares:
        #print i,j,k,i,j+k
        count +=1

print count
print "Time Taken: ", time.time() - start

~/Desktop/python_projects/proj_euler $python prob86.py
1000457
Time Taken:  0.763966083527


Started at 1000, went to 2000, tried 1750, then eventually made my way to 1818 xDD...though fail LOL. Since I'm doing it by the box size, i could have just break out of the loop when i pass 10**6... which I added in. :D;; Jerry logic win.

"""
