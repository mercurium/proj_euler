import time, math
START = time.time()
NUM   = 904961
SIZE  = 10**12
sumz  = 0

for twoPow in xrange(int(math.log(SIZE,2)), 1, -1):
  count = SIZE / 2**twoPow - SIZE / (2 ** (twoPow+1))
  sumz += (NUM+1) * (twoPow - 1) * count

print sumz
print "Time Taken:", time.time() -START


"""
Congratulations, the answer you gave to problem 561 is correct.

You are the 34th person to have solved this problem.


jchen@jchen-mbp 20:28:20 ~/Developer/proj_euler(master) % pypy prob561.py
452480999988235494
Time Taken: 0.000141143798828

Okay, since I'm definitely going to forget this if I don't write this out...

Part 1: Getting the equation for each individual S(p_m^k)

  Testing a few values first, you can get that
  S(p_k) = 3^k - 2^k

  I'm not actually sure why that is true, but I got it by plugging in the first few numbers into oeis, 1,5,21,65

  Going with this pattern, I found:

  S(p_k^2) = 6^k - 3^k

  This was also accomplished by plugging a few numbers into oeis and solving this out.

  At this point, I was sure that `S(p_k^3)` was going to be a similar format.
  S(p_1^3) = 6
  S(p_1^3) = 84

  a   - b   = 6
  a^2 - b^2 = 84
  --> a+b   = 14
  --> a = 10, b = 4

  Okay. At this point I have:
    S(p_k^1) = 3^k - 2^k
    S(p_k^2) = 6^k - 3^k
    S(p_k^3) =10^k - 4^k
  Looks suspiciously like...
    S(p_k^m) = ((m+1)(m+2)/2)^k - (m+1)^k = (m+1)^k * (((m+2)/2)^k - 1)

Part 2: Fast computation of S(p_m^k)
  Def: pow2(num) = largest power of 2 k, such that 2^k | num

  Okay, rolling with the formula from part 1 since project euler doesn't have all that many red herrings in their problems. Not great logic, but hey it looks right.
    S(p_k^m) = ((m+1)(m+2)/2)^k - (m+1)^k = (m+1)^k * (((m+2)/2)^k - 1)
  (I did a bit of testing here before I realized it)
  If we have:
    m % 4 == 1:
      (m+1) / 2 is odd, (m+2) is odd, so S(p_k^m) = 0
    m % 4 == 2:
      (m+1) is odd, (m+2) /2 is even -> ((m+2)/2)^k - 1 is odd -> S(p_k^m) = 0
    m % 4 == 3:
      (m+1) /2 is even, so S(p_k^m) = pow2(m+1/2) * k
    m % 4 == 0:
      Let 4* r = m
      This is the trickiest case, but if you think about the expanded polynomial of ((4r+2)/2)^k - 1, you get:
        (2r+1)^k - 1. The smallest term in the polynomial is `2kr = km/2`
      Since all other terms in this expansion will have larger powers of two than the smalest power in the polynomial,
        so the two power can be determined from that alone.
      -->
      S(p_k^m) = pow2(k * m / 2)

Part 3: Fast computation of S(p_m^k) from k = 1 to 10^12, with k = 904961
  Using part 2, we now know that:
    ( Let m % 4 == 0 )
    S(p_k^(m-3)) + S(p_k^(m-2)) + S(p_k^(m-1)) + S(p_k^m)
  = 0 + 0 + pow2((m-1+1)/2) * k + pow2(m/2)
  = (pow2(m)-1) * k

    Using this information, it's pretty easy to get the rest, figure out the number of m with pow2(m) = 2, pow2(m) = 3, ...etc.

Anyways, with all this said, this was a pretty fun problem. I don't think I was stuck anywhere, and most of it was filled with insights on what else I could do next. Loved the problem and loved how the insights came along.

"""
