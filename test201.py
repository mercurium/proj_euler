import time
start = time.time()

size = 100
arrays = []
arr_len = 100*101*201/6
for i in xrange(51):
	arrays.append([0]*(arr_len))

arrays[0][0] = 1
for i in xrange(1,101):
	for j in xrange(min(i-1,49),-1,-1):
		for k in xrange(0,min(arr_len-i**2,i*(i+1)*(2*i+1)/6)):
			arrays[j+1][k+i**2] += arrays[j][k]
	print i

count = 0
for i in xrange(arr_len):
	if arrays[-1][i] == 1:
		count+=1
print count

print "Time Taken:", time.time()-start
