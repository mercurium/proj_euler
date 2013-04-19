#Conditions:
#GCD(a,b) = GCD(a,c) = GCD(b,c) = 1
#a < b
#a+b =c ---> this makes GCD(a,c)=GCD(b,c) = 1 unnecessary.
#rad(abc) < c
#primes = set of primes
#rad_lst = the radical of the element.
#count = total count for how many elements work

import time
start = time.time()

size = 20000
count = 0
sumz = 0


def gcd(a,b):
  if a == 0:
    return b
  return gcd(b%a,a)


rad_lst = [1]*(size+1)
for i in range(2,len(rad_lst)): #set-up of rad list
  if rad_lst[i] == 1:
    for j in range(i,len(rad_lst),i):
      rad_lst[j]*=i


#if it's prime, then its radical is equal to itself.

def rad_fail(n):
	if rad_lst[n] *6 > n:
		return True
	if rad_lst[n] % 2 == 0 and rad_lst[n] * 15 > n:
		return True
	if rad_lst[n] % 3 == 0 and rad_lst[n] * 10 > n:
		return True
	if rad_lst[n] % 6 == 0 and rad_lst[n] * 35 > n:
		return True
	return False

    

for c in xrange(size):
	if rad_fail(c):
		b = c -1
		if rad_lst[b]*rad_lst[c]< c:
			count +=1
			sumz+=c
			print c-b,b,c
	else:
		#don't need to check even b if c is also even
		diff = -2 if c%2 == 0 else -1 
		for b in xrange(c-1,c//2,diff):
			#we want to avoid checking gcd as much as possible
			if rad_lst[b] == b or gcd(rad_lst[b],rad_lst[c]) != 1: pass
			else:
				if rad_lst[c] * rad_lst[b] * rad_lst[c-b] < c:
					count +=1
					sumz += c
					print c-b,b,c


print ''
print count
print sumz
print "Time Taken:", time.time()-start


"""
...oookay, 108.38 seconds is good enough for me. Now to use java and make it even faster LOL

Original time without enough optimization: ~320 seconds
456
18407904
Time Taken: 258.460896015
Time Taken: 250.037436962 after changing a bit of code, not sure if speedup
Time Taken: 161.858788013 after implementing diff to not check all nums
Time Taken: 108.382901907 using ubuntu, not windows VM
Time Taken: 8.769028862 switched to java LOL

Using 20,000 as a benchmark:
Time Taken: 6.13406205177
Time Taken: 3.79252791405 not checking even b, when c is even
Time Taken: 3.03496789932 getting rid of the isPrime(n) function...25% speedup =.=;;
Time Taken: 2.63325500488 using ubuntu, not windows VM
"""
