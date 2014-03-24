import time
START = time.time()
from primes import *


def get_divisors(n): # returns all divisors of n.
    factors = factor(n)
    divisors = set([1])
    for f in factors:
        new_set = set()
        for d in divisors:
            new_set.add(f*d)
        for i in new_set:
            divisors.add(i)
    return sorted(list(divisors))



sol = set()
max_val = float('inf')
for N in xrange(1,500000):
    if 4*N**3 > max_val:
        break
    Nsqr = N*N+1
    if m_r(Nsqr):
        divisors = [1,Nsqr]
    else:
        divisors = get_divisors(N*N+1)
    for a in divisors:
        b = Nsqr/a
        if max_val > N * (a+N) *(b+N):
            sol.add( N * (a+N)*(b+N))
        else:
            continue
        if len(sol) %1024 == 0 or N % 1024 == 0:
            print len(sol), N
            if len(sol) >= 150000:
                max_val = sorted(sol)[150000 -1]
                print max_val
print len(sol), sorted(sol)[150000-1]

print "Time Taken:", time.time() - START



"""
6: 1, -2, -3        [2,3]         1
42: 2, -3, -7        [2,3,7]        7
120: 3, -5, -8        [2,2,2,3,5]    20
156: 3, -4, -13        [2,2,3,13]    16
420: 4, -5, -21        [2,2,3,5,7]    70
630: 5, -7, -18        [2,3,3,5,7]    105

need n/b + n/c = bc -1

|p| < |q| < |r|
1/pqr = 1/p + 1/q + 1/r
= (pq+qr+pr)/pqr

pq+qr+pr = 1

qr - 1 = pq + qr


pqr = A
pq % (p+q) = 1


pq - 1 = 5p + 5q
pq - Np - Nq - 1 = 0

(p-N)(q-N) = pq - Np - Nq + N^2 

(p-N)(q-N) = N^2+1

pq - 2p - 2q - 1 = 0
(p-2)(q-2) = 2


comes down to solving how many solutions there are for (p-N)(q-N) = N^2+1,

N = 5 -> solutions for 5^2+ 1 = 26, so we have 2*13 -> 7 * 18
1*26 -> 6 * 31 = 186 -> 930

2,5,10,17,26,

Solution:
1884161251122450
Time Taken: 65.8411331177

Congratulations, the answer you gave to problem 221 is correct.

You are the 1188th person to have solved this problem.


OKAY. So the basis of this problem is, we want A = pqr and 1/A = 1/p + 1/q + 1/r
Therefore, 1/pqr = (pq+qr+pr)/pqr
--> pq+qr + pr = 1
--> pq - 1 = 0 mod (qr+pr = r(p+q))
--> we want solutions of the form pq -Np - Nq = 1 
--> (p - N)(q - N) - N^2 = 1
--> (p - N)(q - N) = N^2 + 1
--> want all solutions, and we know that (p - N) * (q - N) = N^2 +1, so therefore p*q >= 4*N^2 (it's smallest if p ~ q), which means that each solution is at LEAST of size:

N* (4N^2) = 4N^3, which means that once our 150,000'th number is < 4N^3, we're done and we have the answer.

Whee, this was a fun problem xDD


 
"""
