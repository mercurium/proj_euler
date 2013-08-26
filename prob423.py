import time
START = time.time()
from bitarray import bitarray

def extended_gcd(a, b): #returns c,d such that ac+bd =1
  if b == 0:
    return (1, 0)
  else:
    q, r = a/b, a%b
    s, t = extended_gcd(b, r)
    return (t, s - q * t)
ext_gcd = extended_gcd

 
size = 10#5*10**7 
is_prime = bitarray('110'+ '01'*(size/2-1)) #0 = prime, 1 = not prime
num_mod = 10**9+7

for i in xrange(3,size,2):
	if is_prime[i] == 0:
		for j in xrange(i**2,size,2*i):
			is_prime[j] = 1



print "Time Taken:", time.time() - START


sumz = 0 
count = 0 #for keeping track of how many primes we've seen so far...

stored = 1

for n in xrange(2,size+1):
	#if n%1024==0: print n
	if is_prime[n] == 0: #number was prime
		count+=1
		stored = (stored * (n-1))%num_mod
		stored = (ext_gcd(count,num_mod)[0]*stored) %num_mod
	else:
 #if the number wasn't a prime, some sequence was ending, so we had to increment the sum
		stored = (stored*5*(n-1))%num_mod
		stored = (ext_gcd(n-count-1,num_mod)[0]*stored )%num_mod	
		#for some reason, there was an extra factor of 5 in the product so this is just to get rid of it.
		if n== 4: stored = stored/5
		
		sumz += stored


print "Time Taken:", time.time() - START


prod = pow(5,n-1,num_mod)
sumz+= prod
for k in xrange(1,count+1):
#	if k%1024 == 0:
#		print k
	prod = (prod * (n-k+1))%num_mod
	prod = (ext_gcd(5*k,num_mod)[0] * prod)%num_mod
	sumz += prod

print (sumz*6)%num_mod
print "Time Taken:", time.time() - START


"""
653972374
Time Taken: 400.618309975
Time Taken: 328.737221003 (got rid of a small inefficiency with using 5^(n-1) % mod rather than pow(5,n-1,num_mod)
Time Taken: 311.028332949 (not even sure what i changed...:/)
YESSSS FINALLY SOLVED ONE OF THE MOST RECENT PROBLEMS

So the first thing I noticed about this problem was that we could compute the number of ways to have exactly k pairs of throws be the same as 6*5^(n-k-1)*ncr(n-1,k) because no matter what, you have 6 choices for the first element, then for the elements not being repeated, you have 5 choices ea. There are (n-k-1) of them not being repeated that are also not the first element. Then for the choice of repeated elements, there are (n-1,k) of them since the first can't be a repeat.

So I tried using this, but of course, ncr(stuff) n^2 times is O(n^3)ish, which is omg ew. What was worse was that I was using ncr(n,r) = n!/(n-r)!r!, which is omg super ewwwwww. So yeah, first I rewrote that then moved on.

Then I noticed that the number of occurences for each entry can be mapped to 6*5^(stuff) * (entry on pascal's triangle). Using the hockey stick formula,

aka: ncr(1,0)+ncr(2,1)+ncr(3,2)+..+ncr(n-1,n-2) = ncr(n,n-2), I managed to get rid of a factor of n from the summation, so that we only had to compute n ncrs rahter than n^2 of them. Thus runtime at this point became O(n^2)

After that, I memoized the ncrs, using the fact that ncr(n,k) = ncr(n-1,k-1)*n/k, bringing the time down even further to O(n). HOWEVER! this is where I ran into my final problem. Large numbers being multiplied are slow. whooops. Yeah. So this was the last problem I had, and to fix it, I used the extended euclidean algorithm to make sure the number stayed small enough to not have to deal with excessively long multiplication times.

With all of that implemented, the runtime dropped dramatically :D, and then I got the answer xDD. (sorry, it's hard to put in graphs here... :/


important info from the debugging:

1 6
2 30 6
3 150 60 6
4 750 450 90
5 3750 3000 900 120
6 18750 18750 7500 1500
7 93750 112500 56250 15000 2250
8 468750 656250 393750 131250 26250
9 2343750 3750000 2625000 1050000 262500
10 11718750 21093750 16875000 7875000 2362500



750 3000 7500 15000 26250
1 4 10 20 35

70

168000

6 6 6 18 (3,1) (ends on 3, 3elt)
30 60 90 180 (4,2) (ends on 5, 4elt)
150 450 900 1500 2250 5250 (7,3) (ends on 7, 5elt)
750 3000 7500 15000 26250 52500 (9,5)
3750 18750 56250 131250 262500 472500


18750 112500 393750 1050000 2362500
93750 656250 2625000 7875000
468750 3750000 16875000
2343750 21093750
11718750
"""
