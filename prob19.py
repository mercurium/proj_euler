import time
START = time.time()

firstDOM = [0,31,59,90,120,151,181,212,243,273,304,334]
lastDOM = [0,31,60,91,121,152,182,213,244,274,305,335]
days = [0,0,0,0,0,0,0]

start = 2 # monday = 1 mod 7, sun = 0 mod 7
count = 0
for year in xrange(1901,2001):
	if ((year % 4 ==0) and (year % 100 != 0)) or year %400 ==0:
		for item in lastDOM:
			days[(start+item)%7] += 1
		start = (start + 366)%7
	else:
		for item in firstDOM:
			days[(start+item)%7] += 1
		start = (start + 365)%7
 
print days

print "Time Taken:", time.time() - START
