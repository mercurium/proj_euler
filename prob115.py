import time
start = time.time()

#we're going to start at n = 3

old = [1]+[0]*49 + [1]
new = [0]*(50+1)

for i in xrange(51,1000):
  new[0] = old[0] + old[-1]
  for j in xrange(1,50):
    new[j] = old[j-1]
  new[50] = old[49]+old[50]
  old = new[:]
  if sum(old)> 10**6:
    break

print sum(old),i
print "Time Taken: ", time.time() - start

"""
~/Desktop/python_projects/proj_euler $python prob115.py
1053389 168
Time Taken:  0.00160503387451

This problem was a simple generalization of problem 114. The concept was the same, look at the last 50 blocks and count from there. Look at #114 for more details on how Jerry solved it back then on 2013/1/20 4:51 am
"""
