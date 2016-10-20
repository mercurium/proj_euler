import time
START = time.time()

expected = 0
probLeft = 1.0
for i in xrange(1,1000):
  expected += i * probLeft / 10
  probLeft *= .9

print expected
print "Time Taken:", time.time() - START



"""
1 digit:
  E(x) = 1 + .9(E(x))
  -> .1 * E(x) = 1
  -> E(x) = 10

2 digit, different:
  E(X) = 1 + .9 * E(X) + .1 * E(Y)
  -> E(X) = 10 + E(Y)


  E(Y)  = .8 * (E(X)+1) + .1 * ( E(Y) + 1) + .1 E(Z)
  -> .9 * E(Y) = .8 * E(X) + .9 + .1 E(Z)
  -> E(Y) = 8/9 * E(X) + 1 + 1/9 E(Z)
  -> E(X) = 10 + E(Y) = 10 + 8/9 E(X) + 1 + 1/9 E(Z)
  -> 1/9 E(X) = 11 + E(Z)
  -> E(X) = 99 + E(Z)

  E(Z) = .8 * (E(X) + 2) + .1 * (E(Y) + 2) + .1 E(ZZ)
  -> E(Z) = .8 E(X) + .1 E(X) + .1 + 1.8 + .1 E(ZZ)
          = .9 E(X) + .1 E(ZZ) + 1.9
  -> E(X) = 1009 + E(ZZ)

I'm really confused on how I want to compute E(min(A,B))

Having additional possibilities should never make the probability higher...


E(X or Y) = E(

"""
