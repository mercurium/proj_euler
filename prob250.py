import time
start = time.time()


power_value = [0]*500
for i in xrange(0,500):
	if i%50 != 0:
		power_value[i] = pow(i%250,i%100,250)
	else:
		power_value[i] = 0

answer_values = [[1] + [0]*249,[0]*250]


for i in xrange(1,250251):
	val = power_value[i%500]
	for position in xrange(0,250):
		answer_values[i%2][position] = ( answer_values[ ( i + 1) % 2 ][position] + \
						  answer_values[ ( i + 1) % 2 ][ (position-val)%250] )   % 10**16
	if i%250==0: print i #just to monitor progress :P

print answer_values[i%2][0]-1
print "Time Taken:", time.time() - start


"""
1425480602091519
Time Taken: 30.8722119331

wowww... stupid a^0=1 errors... =.=;;
"""
