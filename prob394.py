import time
START = time.time()

vals = [0] * 100
for a in xrange(100):
  for b in xrange(100):
    vals[min(a,b)] += 1

val2 = [0] * 100
for c in xrange(100):
  for d in xrange(100):
    val2[c * d/100] += vals[c] * vals[d]

print vals
for i in xrange(10):
  print val2[i*10:10*(i+1)]
print "Time Taken:", time.time() - START


"""
Pr[X=1] = 2p - p^2
Pr[X=2] = ?



Pr[Exactly p left after 1 slice] = (1-p) dx
Pr[Exactly p left after 2 slices] = integral((1-k)(1-p/k) dx^2 from k = p to k = 1

integral((1-k)(1-p/k) dx^2 from k = p to k = 1

integ



"""
