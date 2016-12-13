import time
from primes import ext_gcd
START = time.time()
SIZE  = 10**14
MOD   = 982451653

# Want to find the greatest triangle number less than SIZE
LIM   = int((SIZE*2)**.5)
while LIM * (LIM - 1) / 2 < SIZE:
  LIM += 1

inv = [0,0] + [ (ext_gcd(x, MOD)[0]) % MOD for x in xrange(2, LIM)]

rollingSum = [0] * len(inv)
for i in xrange(2, len(rollingSum)):
  rollingSum[i] = rollingSum[i-1] + inv[i]

print "Time Taken:", time.time() - START

def faMod(n, modNum):
  if n == 0 or n == 1:
    return 1
  numProd = 1
  for i in xrange(2,n+1):
    number = i
    numProd = numProd * number % modNum
  return numProd

# passing in the factorial each time makes it much faster
def computeFact(n, prevComp=0):
  factProd = faMod(n+1, MOD) if prevComp == 0 else prevComp
  factSum  = (rollingSum[n+1] + (inv[2] * inv[n+1] * (n+2))) * factProd
  return factSum % MOD

def computePartial(n, numElem, prevComp=0):
  factProd = faMod(n+1, MOD) if prevComp == 0 else prevComp
  factSum  = (rollingSum[n+1] - rollingSum[n+1 - numElem]) * factProd
  return factSum % MOD

sumz = 10
fa   = 24
for j in xrange(3, LIM):
  if ((j+1)*(j+2))/2 > SIZE:
    break
  sumz += computeFact(j, fa) * (j - 1)
  fa    = (fa * (j+2)) % MOD

endOfTriangles = j*(j+1) / 2 - 1
answer = (sumz + computePartial(j, SIZE - endOfTriangles + 1, fa) * (j-1)) % MOD

print "Answer:", answer
print "Time Taken:", time.time() - START

"""
Congratulations, the answer you gave to problem 374 is correct.
You are the 426th person to have solved this problem.

Return to Problems page.

jchen@jchen-mbp 3:27:38 ~/Developer/proj_euler(master|) % pypy -i prob374.py
Time Taken: 10.5526890755 # generating the inverses for that mod
Answer: 334420941
Time Taken: 16.2453660965

Main thing to note is that the optimal partition is always pretty obvious; we want as many small numbers as possible, creating close to the sequence [2,3,4,5,6,...] as possible

For a specific n, we first can create a partition 2,3,4,5... till it is just below n. Then starting from the end, we add 1 to each of the elements till we hit the limit, or are one away from the limit. If we hit the lim, add one more to the last element.

  Ex: n = 50. Initial sequence = 2,3,4,5,6,7,8,9. We then adjust it to 2,3,5,6,7,8,9,10, which adds up to 50.

  Ex: n = 8. Initial sequence: 2,3. Adjusted -> 3,4. Add on one to the end to get 3,52,3,4,5... till it is just below n. Then starting from the end, we add 1 to each of the elements till we hit the limit, or are one away from the limit. If we hit the lim, add one more to the last element.


  Ex: n = 50. Initial sequence = 2,3,4,5,6,7,8,9. We then adjust it to 2,3,5,6,7,8,9,10, which adds up to 50.

  Ex: n = 8. Initial sequence: 2,3. Adjusted -> 3,4. Add on one to the end to get 3,5

Anyways, it's pretty easy to see what the pattern is after looking at the first few elements, which goes [1], [2], [3], [4], [2,3], [2,4], [3,4], [3,5], [2,3,4], [2,3,5],[2,4,5], [3,4,5], [3,4,6], ...etc.

The next step is to figure out how to sum these up. The numbers in a group actually come out to n! / n, n! / (n-1), n! / (n-2), ... n!/2, so their sum is n! * (1/2 + 1/3+ ... 1/n).

With a rolling sum of inverses of 1/k and a rolling product, this thing comes out to 334420941 mod LARGE_PRIME. YAY

"""
