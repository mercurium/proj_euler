import time
from math import factorial as fa
START = time.time()

SIZE = 100
numPrimes = 25

numWrong = 22
numRight = numPrimes- numWrong

possCounts = dict()
def getTotalCount(a,b,c,d,e): #using i,a,b,c,d,e so it's not long var names
    if (a,b,c,d,e) in possCounts:
        return possCounts[(a,b,c,d,e)]
    if a > numRight or c < 0 or d < 0:
        return 0
    if a == numRight and c == 0 and b+d == numWrong:
        possCounts[(a,b,c,d,e)] = fa(d+e)
        return fa(d+e)
    count = 0
    """place prime in right spot"""
    count += getTotalCount(a+1,b,c-1,d,e)
    """place prime which could be right in wrong spot"""
    count += (c-1) * getTotalCount(a,b+1,c-2,d+1,e)
    """place prime which is already wrong in wrong spot"""
    count += d * getTotalCount(a,b+1,c-1,d,e)
    """place a composite in"""
    count += e * getTotalCount(a,b,c-1,d+1,e-1)
    possCounts[(a,b,c,d,e)] = count
    return count

print getTotalCount(0,0,numPrimes,0,SIZE-numPrimes) *1.0 / fa(100)
print "Time Taken:", time.time() - START

"""
variables that matter:
a--number of numPrimes placed in right slot
b--number of numPrimes placed in wrong slot
c--number of numPrimes not placed which can still be put in right slot
d--number of numPrimes not placed which can not be placed in right slot
e--numComposites left = (100-i) - c -d

a from 0 to 3
b from 0 to 22
c from 0 to 25
d from 0 to 25
e from 50 to 75

first iterate over all prime slots. At each step, pick:
prime in right spot: c -=1, a+=1
prime which could be right in wrong spot: c -=2, b+=1, d+=1
prime which is already wrong in wrong spot: c -=1, b+=1 (d -=1 -> b+=1, c-=1 -> d+=1 --> c-=1, b+=1)
composite: c-=1, d+=1, e-=1

after finishing primes... we multiply by the number of ways to proceed from there,
namely factorial(d+e) (the leftover elements)

a = 3, c = 0, b+d = 22
answer = product / factorial(100)

Congratulations, the answer you gave to problem 239 is correct.

You are the 1115th person to have solved this problem.
~/proj_euler $python prob239.py 
0.00188785484103
Time Taken: 0.0208520889282


Turns out this was one of the problems i just needed to shut up and do. The overall number of possible cases was 4 * 23 * 26 * 26 * 26, which really... is less than 2 million cases, and seriously, not all of those would be covered. I could have solved this sooner if i just enumerated all the variables I needed and plugged it in

"""
