import time
START = time.time()

numDig   = 10
prevCountArray = [ [0,0] + [1] * 9 + [0],   \
                   [0,0] + [1] * 8 + [0,0], \
                   [0,0] + [1] * 8 + [0,0], \
                   [0,0] + [1] * 9 + [0]    \
                 ]

cumm_sum = 0
for i in xrange(0,39):
  counts      = [0]*4
  countsArray = [ [0] * 12 for uniqueVarName in range(4) ]

  for j in xrange(1,numDig+1):
    for k in xrange(4):
      if ( (k not in [1,2] or j != numDig) and (k not in [2,3] or j != 1)):
        countsArray[k][j] = prevCountArray[k][j-1] + prevCountArray[k][j+1]

    for k in xrange(4):
      counts[k] += countsArray[k][j]

  prevCountArray = countsArray
  cumm_sum += counts[0] - counts[1] + counts[2] - counts[3]
  print "iteration:", i+2, "\tcount:", cumm_sum
print "The answer is:", cumm_sum

print "Time Taken:", time.time() - START

#Okay, so the way this problem can be solved is by realizing that if you want to have 0-9, you either need 0123456789 or 9876543210 in there. Then once you have that, you can either insert more in the middle of the steps or add to the ends.


'''
The answer is: 126461847755
Time Taken: 0.00176191329956

'''
