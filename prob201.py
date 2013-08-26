import time
START = time.time()

SIZE = 100
NUM_PRIMES = 50

def sum_sq(n):
	return n * (n+1) * (2*n+1)/6

arr_len = sum_sq(SIZE) #Sum of the square from 1 to 100 (1^2 + 2^2 + 3^2 +...+100^2)
arrays = [ [0] * (arr_len) for i in xrange(NUM_PRIMES + 1) ]

arrays[0][0] = 1  #First index implies how many numbers are in it,

for i in xrange(1,SIZE + 1):  #For each square from 1 to 100
	for j in xrange(min(i-1,NUM_PRIMES-1),-1,-1): #number of primes used, going in reverse to avoid compounding adds.
		#We don't need to check all indices, only up to a certain SIZE. Either up to the end of the array if we have large numbers, or until what could have occured already.
		for k in xrange( 0 , min(arr_len-i**2, sum_sq(i) )  ):
			arrays[j+1][k+i**2] += arrays[j][k]
	print i

sumz = 0
for i in xrange(arr_len):
	if arrays[-1][i] == 1:
		sumz += i
print sumz
print "Time Taken:", time.time()-START


"""
115039000
Time Taken: 136.413109064


"""
