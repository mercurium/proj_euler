import time
start = time.time()

count = 0
size = 100

vals = dict()

def euclid(a, b): #returns c,d such that ac+bd =1
	if b == 0:
		return 0
	else:
		return euclid(b,a%b) + 1
ext_gcd = euclid

for i in xrange(1,size+ 1):
	for j in xrange(1,i + 1):
		if i == j:
			count += ext_gcd(i,j)
		else:
			count += 2*ext_gcd(i,j)+1

print count

print "Time Taken", time.time() - start

"""

OH YEAHHHH.... I forgot. I wrote this one using C++ since it was taking so long with python.... :D;;;


"""
