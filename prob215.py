import time
START = time.time()

combinations = [0,0,1,1]
for i in xrange(30):
	combinations.append(combinations[-2] + combinations[-3])

print combinations
print combinations[32]
print "Time Taken:", time.time() - START
