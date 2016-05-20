import time
start = time.time()
"""
f(5) = 30
f(10) = 138
f(1000) = 1177848
"""

size = 10**8
arr = [0]*(size+1)
sumz = 0
for i in xrange(2,size+1):
  if i > size/2: break
  if arr[i] == -1: #number isn't squarefree, we don't want it.
    continue
  a = size//i #size of orchid that we're adding on

  if arr[i] == 0:
    for j in xrange(2*i,size/2,i):
      #ignore the number if it isn't squarefree.
      if arr[j] != -1: arr[j] += 1
    sumz += a*(a-1)/2
    #print i, a*(a-1)/2

  #this marks a number as a square, and all of its future nonsquarefree terms.
  elif arr[i] == 1:
    for j in xrange(2*i,size/2,i):
      arr[j] = -1

  #if it has an odd # of factors, add it back on
  elif arr[i]%2 == 1:
    sumz += a*(a-1)/2

  #even number of prime divisors, want to subtract it off
  elif arr[i]%2 == 0:
    sumz -= a*(a-1)/2



#Since we're only computing it for each little triangle, multiply result by 6 to get answer, then add the edges.
print "actual sum:", sumz*6+(size-2)*6
print "Time Taken:", time.time() - start


"""
actual sum: 11762187201804552
Time Taken: 104.268545866
Time Taken: 88.0409138203 (made it stop once it passed size > 2)
Time Taken: 58.2007551193 (made program not increment counter on numbers > size/2)
Time Taken: 1.524619189 (wrote it in java...)
Time Taken: 1.361989529 (changed to bytes...)
So the idea behind this was, the only time a point (x,y) is not able to be seen from the origin is if gcd(x,y) = d != 1. Then (x/d,y/d) is in the way.

Basically, the number of ways to have blocked points is the number of ways we can block them.... err. So if we want to block (2x,2y) with (x,y), we need to find the # of points in the hexagonal orchid of size/2.

So we want to add up # of points in size/2 + size/3 + size/5 + size/7 + ...etc.

HOWEVER, numbers like 6 = 2*3 get counted twice, so we need to subtract them off. Also numbers like 4 = 2*2 don't need to be counted.

So if odd # of prime factors, add it, if even: subtract it, though ignore if not squarefree.

Using idea of P(A or B) = P(A) + P(B) - P(A and B)

"""
