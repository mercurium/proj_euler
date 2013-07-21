import string
import math
import time
start = time.time()

def approx_pow(n,powz,dig):
        if powz == 0: return 1
        if powz == 1: return truncate(n,dig)

        val = int(math.log(powz,2))
        lst = [1,n] + [0] * val
        for i in xrange(2,len(lst)):
                lst[i] = truncate(lst[i-1]**2,dig)

        pows = [0] * (val+1)
        power = powz
        for i in xrange(0,len(pows)):
                pows[i] = power % 2
                power = power //2
        product = 1
        for i in xrange(0,len(pows)):
                if pows[i] == 1:
                        product = truncate(product * lst[i+1],dig)
        return product

def truncate(num, dig):
        num_len = int(math.log(num,10))
        if num_len < dig:
                return num
        return num/10**(num_len -dig)


mod = 10**9
vals = (1,1)
a = (5**.5+1)/2

def find_L(n):
	approx_head = int(truncate(approx_pow(a,n,50)/(5**.5),8))
	val = string.join(sorted(str(approx_head)),'')
	return  (val  == '123456789', val, approx_head)

for i in xrange(3,5* 10**5):
	vals = (vals[1],(vals[0]+vals[1])%mod)
	if string.join(sorted(str(vals[1])), '') == "123456789":
		L_works, value,junk = find_L(i)
		if L_works: 
			print i
			break
		else:
			print "so close, but on:", i, value, junk

print "Time Taken: ", time.time()-start


"""
"""
