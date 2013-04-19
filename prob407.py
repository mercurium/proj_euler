#IMPORTANT! If a^2 = a mod n, then a(a-1) = 0 mod n, and thus a = 1 for primes.

import time
start = time.time()
size = 10**7

pfactor = range(0,size+1)
for i in xrange(2,len(pfactor)):
  if pfactor[i] == i:
    for j in xrange(i*2,len(pfactor),i):
      pfactor[j] = i
      

def calc(n):
  if pfactor[n] == n: return 1
  for i in xrange(n - pfactor[n], n/2-1, -1 * pfactor[n]):
    a = i**2
    if (a + i) % n == 0: return i+1
    if (a - i) % n == 0: return i
  return 1


sumz = 1
for i in xrange(2,size+1):
  val = calc(i)
  sumz += val
  if i%(2**16) == 0: print i
print sumz
print "Time Taken: ", time.time() - start

"""
...LOL
39782849136422 is the wrong answer I got after 
Time Taken:  5072.10592484 using laptop
Time Taken:  677.419348955 using desktop and not printing as much... wat
Time Taken:  83.780217283 (using java LOL)
Time Taken:  60.615508996 (using java, not printing at each step)
...aka, 1.4 hrs LOL

LOL LOL LOL I HATE MYSELF. I REREAD THE QUESTION AND f(1) = 0, NOT f(1) = 1. BASICALLY I DIDN'T TURN THIS PROBLEM IN FOR A MONTH BECAUSE OF AN OFF BY ONE ERROR.... TT____TT
39782849136421 is the right answer

Size: 10**6
Time Taken:  22.355866909 (with prints once every 1024 statements)
Time Taken:  63.4468739033 (size 2*10**6)
"""
