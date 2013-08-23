import time
START = time.time()

lst = [0] * (10**7)

for i in xrange(2,len(lst)):
	for j in xrange(i, len(lst), i):
		lst[j] += 1

count = 0
for i in xrange(2,len(lst)-1):
	if lst[i] == lst[i+1]:
		count += 1
print count
print "Time taken:", time.time() - START

"""
~/Desktop/python_projects/proj_euler $python prob179.py
986262
Time Taken: 64.1562099457
Time Taken: 45.9769480228
"""
