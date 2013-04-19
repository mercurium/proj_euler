import time
start = time.time()

def gcd(a,b):
  while b:
    a,b = b, a%b
  return a

size = 10

sumz = 0
ratio = [1]*(size+1)
for i in xrange(2,size):
  if ratio[i] == 1:
    for j in xrange(i,size-i+1,i):
      ratio[j] *= (i-1.)/i
  ratio[i] = 1-ratio[i]
  print i,int(min(i,size-i) * ratio[i]), ratio[i]
  sumz += int(min(i,size-i) * ratio[i])
sumz *=6
print sumz
print "Time Taken: ", time.time() - start



"""

count = 0
for i in xrange(1,size+1):
  for j in xrange(1,min(i,size-i+1)):
    if gcd(i,j) != 1:
      count+=2
count += 3*size/2 -2
count *=6
print count
print "Time Taken: ", time.time() - start
"""

"""
Okay, well. As of 1/25, I've figured out how to count the number of ways the points that are hidden. Basically, they're the ones where gcd(a,b) != 1, aka n/k --> (n/a)/(k/a). This can be explained as some point in that angle has been seen before. Then we can multiply the answer by 6 to get it fully under rotation.

"""





