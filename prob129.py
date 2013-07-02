
import time
start = time.time()

for num in xrange(10**6,10**6+10**5):
	if num % 2 == 0 or num %5 == 0:
		continue
	print num
	broken = False
	sumz = 1
	for powz in xrange(1, 10**6+1):
		sumz = (sumz + pow(10,powz,num))% num
		if sumz == 0:	
			broken = True
			print num, powz
			break
	if not broken:
		print num, 'DONE'
		break	
print "Time Taken:", time.time()-start
