import time
start = time.time()

def slow_comp(n):
  lst = [1]
  for i in range(2,n):
    if i**3 % n == 1:
      lst += [i]
  return lst

def extended_gcd(a, b): #returns c,d such that ac+bd =1
  if b == 0:
    return (1, 0)
  else:
    q, r = a/b, a%b
    s, t = extended_gcd(b, r)
    return (t, s - q * t)
ext_gcd = extended_gcd

#this takes a set of values and bases so that we can find x s.t.
#x = a1 mod b1
#x = a2 mod b2
#... and so on for any number of bases

def crt(bases, vals):  
  big_base = 1
  sumz = 0
  for val in bases: big_base *= val
  for i in range(0,len(bases)):
    curr_base = big_base / bases[i]
    inverse = ext_gcd(bases[i],curr_base)[1]
    sumz += vals[i] * curr_base * inverse
  return sumz % big_base


fixed_val = 153416670
changers = [7,13,19,31,37,43]
change_val = [[1,2,4],[1,3,9],[1,7,11],[1,5,25],[1,10,26],[1,6,36]]


fixed_val = 153416670
changers = [7,13,19,31,37,43, fixed_val]
cv = [[1,2,4],[1,3,9],[1,7,11],[1,5,25],[1,10,26],[1,6,36]]

sumz = 0
for a in xrange(3):
  for b in xrange(3):
    for c in xrange(3):
      for d in xrange(3):
        for e in xrange(3):
          for f in xrange(3):
            val = crt(changers, [cv[0][a],cv[1][b],cv[2][c],cv[3][d],cv[4][e],cv[5][f],1])
            if val != 1: sumz += val
print sumz

print "Time Taken:", time.time() -start

