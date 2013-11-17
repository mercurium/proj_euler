import math
import time
start = time.time()
n = 10**6



count = 0
i = 2
while (n - i**2)/(2*i) > 0:
  count = count + (n - i**2)/(2*i)
  #print (n - i**2)/(2*i)
  i = i +2


print count
print "Time Taken:", time.time() - start
"""
22:38 ~/Desktop/python_projects/proj_euler $ python prob173.py 
1572729
Time Taken: 0.000257968902588
"""
