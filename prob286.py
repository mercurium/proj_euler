import time
start = time.time()

def val_calc(q):
	lst = [1] + [ (1-x/q) for x in xrange(1,51)]
	prob = [1]+[0]*50
	new_prob = [0]*51
	for i in xrange(1,51):
		new_prob[0] = prob[0] * (1.-lst[i])
		for j in xrange(1,51):
			new_prob[j] = prob[j]*(1.-lst[i])+prob[j-1]*lst[i]
		prob = new_prob[:]
	return prob[20]

print val_calc(50.)
print "Time Taken: ", time.time() - start

sumz = 50.
val = val_calc(50.)
digz = -1
for i in xrange(0,11):
	for dig in xrange(0,10):
		num = sumz + dig/10.**i
		if val_calc(num) < .02:
			break
		if val_calc(num) < val:
			val = val_calc(num)
			digz = dig
	sumz += digz/10.**i
	print sumz

print sumz
print "Time Taken: ", time.time() - start
"""
>>> val_calc(52.64945719530)
0.020000000000052105

Congratulations, the answer you gave to problem 286 is correct.

You are the 973rd person to have solved this problem.


So I was too lazy to write a program to compute it so I just did it by hand lololol.
Anyways umm... So given a probability of scoring at each point, we can compute the chance of getting exactly 20 shots in pretty easily. As such, we just need to plug in the right probability and we're done. Now how do we find the probability of scoring? Well, we check all possibilities =P. First .1, then .2, then .3, ...etc. After we reach .9 (say it was closesst at .2), then we check .11, .12, .13, ..., .21, .22, .23, and so on so forth. Then we append a third digit and check all of those as well. As a result, we get increasingly closer and get the 10 digits as requested.

"""
