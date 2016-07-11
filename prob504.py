import time
START = time.time()
SIZE  = 100

squares = set([x**2 for x in xrange(1,141)])

def computeCosts(lim):
  costDict = dict()
  for a in xrange(1, lim+1):
    for b in xrange(1, a+1):
      costDict[(b,a)] = sum([ (a*c - 1) / b for c in xrange(1,b)])
  return costDict

costDict = computeCosts(SIZE)

count = 0
for a in xrange(1,SIZE+1):
  for b in xrange(1,SIZE+1):
    for c in xrange(1,SIZE+1):
      for d in xrange(1,SIZE+1):
        total_cost = \
              costDict[(min(a,b), max(a,b))] \
            + costDict[(min(b,c), max(b,c))] \
            + costDict[(min(c,d), max(c,d))] \
            + costDict[(min(d,a), max(d,a))] \
            + a+b+c+d-3
        if total_cost in squares:
          count += 1
  print a

print "Answer is:", count
print "Time taken:", time.time() - START

'''

Congratulations, the answer you gave to problem 504 is correct.
You are the 1438th person to have solved this problem.

694687
Time taken: 37.2965099812



'''
