import time
START   = time.time()
NUM_BIN = bin(10**12/4)[2:]

sumz    = 0
twoMult = 0
for index in xrange(len(NUM_BIN)):
  if NUM_BIN[index] == '0':
    continue
  sumz += 3**(len(NUM_BIN) - 1 - index) * 2**twoMult
  twoMult += 1

print sumz
print "Time Taken:", time.time() - START

"""
Congratulations, the answer you gave to problem 242 is correct.

You are the 723rd person to have solved this problem.

jchen@jchen-mbp 10:26:43 ~/Developer/proj_euler(master) % pypy prob242.py
997104142249036713
Time Taken: 0.000201940536499


The number of solutions for a given n, over all k is given by the OEIS sequence: A001316
let a(n) = nth value.
Starting few values: 1,2,2,4,2,4,4,8

2 x a[0:2^n-1] = a[2^n:2^(n+1)-1]

Since we're doubling the value each chunk of 2^n, we get that sum(first 2^n) = 3 x sum(first 2^(n-1))

More intersting though, is since we have that pattern above, we can do stuff like...

a(53) = 2 a(53-32) = 2 a(21) = 4 a(21-16) = 4 a(5) = 8 a(1) = 8 x 2 = 16.
bin(53) = '0b110101', which has 4 1's

And in general, a(n) = 2^number of 1's in its binary expansion

Then, since we're summing over a whole sequence, we know that sum(1 to 2^n) = 3 sum(1 to 2^(n-1))
  -> sum(1 to 2^n) = 3^n, and if we need to left shift (say summing from 2^10 to 2^10 + 2^4),
  we know that seq(2^10 to 2^11-1) = 2 seq(1 to 2^10 -1)
  -> sum(2^10 to 2^10+16) = 2 x sum (0 to 16)
  -> 2 x 3^4 = 162

And yeah, change the number, 10^12 / 4 into binary, use the above idea, and you get the solution \o/.
  I missed a karate class to solve this problem, but totally worth :D



f(n,k) = sum(ncr(n/2+1,j) x ncr(n/2, k-j) ) for j = range(1,k+1,2)

Can skip n if n%4 != 1
Can skip if k%4 != 1

f(n,n) = 1 for all n where n % 4 = 1

let a(n) = nth value.
Starting few values: 1,2,2,4,2,4,4,8

2 x a[0:2^n-1] = a[2^n:2^(n+1)-1]



"""
