#NOTE TODO need to solve it
import time, math
START = time.time()
POWER = 18
SIZE  = 10 ** POWER

count = [1,10]

for dig in xrange(2, POWER + 1):
  tempCount = 0
  for digLen in xrange(2, dig + 1):
    for start in xrange(0, dig - digLen + 1):
      tempCount += count[start] * (10**(dig - start - digLen) \
        - sum([10**x for x in range(dig - start - digLen)]))

  count.append(9* 10**(dig-1) - tempCount + count[-1])

print count
print count[-1], SIZE-count[-1], math.log(SIZE-count[-1],10)
print "time taken:", time.time() - START

print "okay, so that's the majority of them, now for the rest..."

count     = 0
for i in xrange(1,10**8 +1):
  if '11' not in str(i) \
      and '121' not in str(i) \
      and '1331' not in str(i) \
      and '14641' not in str(i) \
      and '161051' not in str(i) \
      and '1771561' not in str(i) \
      and '19487171' not in str(i):
    count += 1
  if i in [10,10**2, 10**3, 10**4, 10**5, 10**6, 10**7]:
    print i, count

print count



"""
19:35 ~/Desktop/python_projects/proj_euler $ python prob442.py
[1, 10, 99, 979, 9681, 95734, 946705, 9361892, 92579038, 915507091, 9053380277, 89528191841, 885337508138, 8755035561431, 86577883549894, 856162132910112, 8466522485580903, 83724799595140123, 827948201777605653]
827948201777605653 172051798222394347 17.2356592161
time taken: 0.00135016441345
okay, so that's the majority of them, now for the rest...


1        = 1
10       = 10
99       = 100  - 1 x 10^0
980      = 10^3 - 2 x 10^1
9701     = 10^4 - 3 x 10^2 +  1 x 10^0
96030    = 10^5 - 4 x 10^3 +  3 x 10^1
950599   = 10^6 - 5 x 10^4 +  6 x 10^2 - 1  x 10^0
9409960  = 10^7 - 6 x 10^5 + 10 x 10^3 - 4  x 10^1
93149001 = 10^8 - 7 x 10^6 + 15 x 10^4 - 10 x 10^2 + 1
922080050= 10^9 - 8 x 10^7 + 21 x 10^5 - 20 x 10^3 + 5 x 10^1

1
1 1
1 2 1
1 3 3 1
1 4 6 4 1
1 5 10 10 5 1
1 6 15 20 15 6 1
1 7 21 35 35 21 7 1
1 8 28 56 70 56 28 8 1


"""


