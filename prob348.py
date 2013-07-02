import time
start = time.time()

vals = dict()

a,b = 80000,1000

sqs = [x**2 for x in xrange(a)]
cus = [x**3 for x in xrange(b)]

vals = dict()
count, sumz = 0,0

for i in xrange(a):
	if i%1024 == 0: print i
	if count == 5:
		break
	for j in xrange(b):
		if count == 5:
			break
		ij = sqs[i] + cus[j]
		if str(ij) == str(ij)[::-1]:
			if ij in vals:
				vals[ij] +=1
				if vals[ij] >= 4:
					sumz += ij
					count +=1
			else:
				vals[ij] = 1

print sumz
print "Finish Time:", time.time() -start


"""
5229225
37088073
108909801
796767697
29142024192

1004195061
Finish Time: 18.6743748188

"""
