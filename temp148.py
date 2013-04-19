import math
import time


start = time.time()
size = 64
num = 2
triangle = [ [1] * (x+1) for x in range(0,size+1)]

for i in range(1,len(triangle)):
  for j in range(1,len(triangle[i])-1):
    triangle[i][j] = (triangle[i-1][j] + triangle[i-1][j-1]) %num

count = 0

for i in range(0,len(triangle)):
  print ' '*(size - i),
  for j in range(0,len(triangle[i])):
    if triangle[i][j] == 0:
      print 0,
      count +=1
    else:
      print ' ',
  print ' '*(size - i), i, ' ',  count


print "time elapsed = " + str(time.time()-start)


#size of each triangle is...
# n(n-1)/2, n^2(n^2-1)/2, n^3(n^3-1)/2
#for the case of n = 3, this is 3, 36, 351, ...
#so the size of each subsection becomes...

#Each number is going to show up n times for a m(m-1)/2 triangle for some m

#9 = a1 *n(n-1)/2 = a1^2
#162= a2 * n(n-1)/2 + a1^2 * (n * (n+1)/2) = a1*a2 + a1^2 * n(n+1)/2



