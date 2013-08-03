import time
start = time.time()

SIZE = 10**5


def real_num(size):
	sumz = 0
	for i in xrange(1,size+1):
		sumz += (size//i) * i	

	return sumz	

def complex_num(size):
	sumz = 0
	seen = set()
	for i in xrange(1,int(size**.5)+1):
		a = i **2
		for j in xrange(i,size+1):
			b = j**2
			if a + b > size:
				break
			for k in xrange(1,size+1):
				if k*(a+b) > size:
					break
				if (i*k,j*k) in seen:
					continue
				seen.add((i*k,j*k))
				if i == j:
					sumz += (2 * i * k) * (size/ ((a + b) * k ))
				else:
					sumz += (2 * (i+j) * k) * (size/ ((a + b) * k ))
#				print complex(i*k,j*k), (2 * i * k) * (size/ ((i**2 + j**2) * k ))
		#print i
	return sumz	

def test():
	print "Test case for 5 is:",  (real_num(5) + complex_num(5) == 35 ) 
	print "Test case for 10^5 is:", (real_num(10**5)+ complex_num(10**5) == 17924657155 )

#test()
R = real_num(SIZE)
print "Time Taken: ", time.time() - start
C = complex_num(SIZE)
print "Total is:", R+C
print "Time Taken: ", time.time() - start

"""
This can be calculated by calculating the real_num numbers and the complex_num numbers separately. 


...except oh boy. This problem is harder than I expected.

If (1+2i) divides 5, then it also divides 10,15,20, etc... I forgot about that case... sigh....

"""
