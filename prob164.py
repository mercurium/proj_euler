import time
START   = time.time()
SIZE    = 10
NUM_DIG = 20

chart   = [ [0] * SIZE for x in xrange(SIZE)]
chart2  = [ [0] * SIZE for x in xrange(SIZE)]

for i in xrange(1,len(chart)):
  chart[i] = [1] * (SIZE - i) + [0] * i

for loops in xrange(0, NUM_DIG-2):
  for k in xrange(0,SIZE):
    for i in xrange(0,SIZE-k):
      for j in xrange(0,SIZE-i-k):
        chart2[j][k] += chart[i][j]
  chart  = chart2
  chart2 = [ [0] * SIZE for x in xrange(SIZE)]


sumz = sum([sum(row) for row in chart])

print sumz
print "Time Taken:", time.time()-START
assert(sumz == 378158756814587)



#for the beginning, we use first to denote the number of ways to pick a first digit. Obviously # of ways to pick the first digit for each first digit = 1 (besides 0 since we don't have leading zeroes)

#then we can compute the possible second digits. After that, we make an n by n chart keeping track of all endings. Since we only care about the last two digits, we keep a chart of how many numbers end with a certain sequence. We update this the required number of times (20). and get the answer: 378158756814587
