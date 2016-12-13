import time
START = time.time()
SIZE  = 123456789

def diffAB(n):
  startVal = (sum(1./i for i in xrange(1,n+1)))
  for i in xrange(n):
    startVal /= 2
    if startVal < .1:
      startVal *= 10
  return startVal

uncleanedAnswer = diffAB(SIZE)
answer          = str(uncleanedAnswer)[2:9]

print "Answer:", answer
print "Time Taken:", time.time() - START

"""

Congratulations, the answer you gave to problem 568 is correct.

You are the 11th person to have solved this problem.

jchen@jchen-mbp 10:45:26 ~/Developer/proj_euler(master|✚2…) % pypy prob568.py
0.422802031896
Time Taken: 1.2033700943

Since this overlapped with problem 567 so much, look there for more info on how to solve this one.

Since we have these:
  A(n) = A(n-1)/2 + 1/n - 1/(2^n * n)
  B(n) = B(n-1)/2 + 1/n

B(n) - A(n) = (B(n-1) - A(n-1))/2 - 1/2^n * (1/n)
            = (B(n-2) - A(n-2))/4 - 1/2^n * (1/n + 1/(n-1))
            = (B(n-3) - A(n-3))/8 - 1/2^n * (1/n + 1/(n-1) + 1/(n-2))
            ...
            = (B(1) - A(1)/2^(n-1) + (sum(1/i) from i in xrange(2,n+1))/2^n)
            = ( (1/2)/2^(n-1) + (sum(1/i) from i in xrange(2,n+1))/ 2^n)
            = (1/2^n) * sum(1/i) from i = 1 to n
---> deal with precision errors, and we're golden

"""
