import time
START = time.time()

def gcd(a,b):
    while a != 0:
        a,b = b%a, a
    return b

k = 13
for n in xrange(5,10**4):
    a = gcd(k,n)
    k += a
    if a != 1:
        if a != n:
            print n,k,a
        else:
            print n,k,a, '\t\t OMG IT WORKS'

print "Time Taken:", time.time() - START

START = time.time()

SIZE = 10**15
last_k = k = 13
last_n = n = 5
count = 0
prev = 0
while n < SIZE:
    if count == 10**7/2 or (n < 16*10**11 and count >= 100000/2):
        count = 0
        if n < SIZE/2:
            n = last_n = last_n * 2 -1
            k = last_k = last_n * 3
            print n, k, "RAWR!", n/2 - prev
            prev = n
            n+=1
            continue
        else:
            break
    a = gcd(k,n)
    k += a
    count +=1
    if a != 1:
        last_n = n
        last_k = k
    n += 1

print last_n, last_k, "answer seems related to this"

print last_k + (SIZE - last_n)
print "Time Taken:", time.time() - START

"""

9 18 9
17 34 17
41 82 41
83 166 83
167 334 167
353 706 353
761 1522 761
1523 3046 1523
3119 6238 3119
6257 12514 6257
12539 25078 12539
25121 50242 25121
50291 100582 50291
101141 202282 101141
202817 405634 202817
405641 811282 405641
812051 1624102 812051
1624151 3248302 1624151
3248303 6496606 3248303
6496943 12993886 6496943


Congratulations, the answer you gave to problem 443 is correct.

You are the 112th person to have solved this problem.

Nice work, mercurium, you've just advanced to Level 9.
864 members (0.26%) have made it this far.


2744233049300770
Time Taken: 87.8681638241

okay, so the writeup...
I have to admit, I did not like my solution very much... it was quite hacky...

Anyways, what I noticed for this was:
if we have gcd(g,n) != 1, then we increment by more than one. However, the number of times we do it is quite limited (someone on forums mentioned that it's ~300 times max.

So the interesting thing to note (not related to solving it) is that if gcd(g,n) != 1, then g+gcd(g,n) = 3n... weird as heck.

Also, the solutions seem to cluster together, and only work once every doubling of n. Thus, we can skip most of the fluff in the middle for the numbers that aren't important (if 353 works, the next few are going to be around 700 something).

I also noticed that if 382 was the last one in the cluster to work, then the following cluster would start with 761, aka, 2 * last - 1. Not sure why this happens, but hey, pretty cool :P

So... yeah, should have done this yesterday =.=;; It only took me ~2 hours... T_T;;
"""
