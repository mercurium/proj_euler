
SIZE = 8

def arrayGen(i):
  n = []
  while i > 0:
    n.append(i%2)
    i /= 2
  return n

sumz = 0
for j in xrange(1,SIZE):
  n    = arrayGen(j)
  base = 1
  while sum(n) > 0:
    #print n, base
    if n[0] > 0:
      base += n[0]
      n[0]  = 0
    else:
      base += 1
      index = min([index if n[index] != 0 else 100 for index in xrange(len(n))])
      n[index] -= 1
      for i in xrange(0,index):
        n[i] += base

  print j, base - 1
  sumz += base - 1

print sumz


"""

1 1
2 3
3 5
4 21   (2+1) x 2^3 - 3
5 61   (3+1) x 2^6 - 3
6 381  (2+1) x 2^7 - 3
7 2045 (3+1) x 2^9 - 3
8 2^(2^23
2517


"""
