import time
start = time.time()


precompute = [0]*500
for i in xrange(0,500):
	if i%50 != 0:
		precompute[i] = pow(i%250,i%100,250)
	else:
		precompute[i] = 0

vals = [[1] + [0]*249,[0]*250]


for i in xrange(1,250251):
	val = precompute[i%500]
	for j in xrange(0,250):
		vals[i%2][j] = (vals[(i+1)%2][j] + vals[(i+1)%2][(j-val)%250])%10**16
	if i%250==0: print i

print vals[i%2][0]-1
print "Time Taken:", time.time() - start


"""
1425480602091519
Time Taken: 30.8722119331

wowww... stupid a^0=1 errors... =.=;;
"""
