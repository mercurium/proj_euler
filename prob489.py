#NOTE TODO need to solve it
import time

START    = time.time()
SIZE_LIM = 10**5
A_LIM    = 10
B_LIM    = 10

def gcd(a,b):
  while b:
    a,b = b, a%b
  return a

def GD(a,b,n):
  return gcd(n**3 + b, (n+a)**3 + b)

def getRoughEst(a,b):
  maxN   = 1
  maxVal = 1
  n      = 0

  while n < SIZE_LIM * (1 if (a < 6 ) else 3*10**3):
    num = GD(a,b,n)
    if num > maxVal:
      maxN   = n
      maxVal = num
      #print n, num
    n += maxVal
  return { 'maxN' : maxN, 'maxVal' : maxVal }

def getMaxN(a,maxN, maxVal):
  for n in xrange(maxN, 0, -maxVal/a):
    if GD(a,b,n) == GD(a,b,maxN):
      maxN = n
  return maxN


sumz = 0

for a in xrange(1,A_LIM + 1):
  for b in xrange(1,B_LIM + 1):

    #This part find the maxVal, but doesn't guarantee that maxN is as small as possible
    roughEst = getRoughEst(a,b)
    maxVal   = roughEst['maxVal']
    maxN     = roughEst['maxN']

    #This part goes back to check that maxN is as small as possible. Should be a fast check.
    maxN     = getMaxN(a, maxN, maxVal)

    #Accumulate the sum of maxN from earlier
    sumz += maxN

    print a,'\t', b,'\t', maxN,'\t', maxVal
    #print '==============================='

print sumz
print "Time Taken:", time.time() - START

"""
(n+a)^3 + 1 = n^3 + 3an^2 + 3a^2n + 1

gcd(3an^2 + 3a^2n+a^3, n^3+1)

gcd(a(3n^2 + 3an + a^2), (n+1)(n^2-n+1)

gcd(3n^2 + 3n + 1, (n+1)(n^2-n+1)

gcd(3n^2a + 3na^2 + a^3, n^3 + b)

1   1   5       7
1   2   51      109
1   3   56      61
1   4   210     433
1   5   161     169
2   1   101     182
2   2   52      86
2   3   113     614
2   4   44      124
2   5   459     1478
3   1   17      63
3   2   55      93
3   3   3       3
3   4   5       129
3   5   28      39
4   1   3219    16492
4   2   1640    2102
4   3   6913    17356
4   4   316     1132
4   5   743     19084
5   1   16119   19565
5   2   65132   78665
5   3   4123    19835
5   4   29221   80285
5   5   95      815


We are guaranteed these two statements: (no proof, but it looks like it's true, and that's the way euler problems work)

GD(n) := gcd(n^3+b, (n+a)^3+b)
N     := n where GD(n) is maximized

forall i:
  GD(i)  | (N - i) * a
  GD(i)  | GD(N)
  maxVal | a

So we know how to find a larger solution given the smaller ones. ...well, minor addendum to that. Need to divide by a to make it true.

errors on (4,4), (3,1), (2,4)
(4,4): expected: (1132,316) actual: (1132,882)
(3,1): expected: (63,17)    actual: (63,38)
(2,4): expected: (124,44)   actual: (124,106)

"""
