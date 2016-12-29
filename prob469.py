import time, math
START = time.time()
SIZE  = 10**7

#vals = [0.0, 1., 1., 1., 2.]
vals = [0.0, 1., 1.]

for i in xrange(3, SIZE+1):
  prob = (2*vals[-2] + (i-1)*vals[-1] + 1) / i
  if i % 2**20 == 0:
    print prob, [(1 - (1.+prob) / (i+3))]
  vals.append(prob)
  vals.pop(0)

print [1 - (1+ vals[i]) / (SIZE-len(vals) + i + 4) for i in xrange(len(vals))]
print (1+vals[-1])/ SIZE
print "Time Taken:", time.time() - START




"""

0 1 2 3 4

2 3 4

2 -> () / (4)

3 -> () / ()



xrange(1,3) -> [1,2]

E(x) = 1 - (1/k) (1+g(k-3))

g(k) = 1 + sum(2 * g(m)) from m = 1 to m = (k-2)

g(k) = 1/k + 2g(k-2)/k + (k-1)g(k-1)/k

Looks suspiciously like the continued fration [1,1,3,5,7,9,11,13,15,17,19,...]


"""
