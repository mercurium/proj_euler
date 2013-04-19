#so since 27 is the smallest odd # for which this doesn't work, the largest this could be is (124*2 -1) * 27 = 6669
import time
start = time.time()

n = 25
a = [1,1,3]
count = 0
rounds = 0
while rounds < 124:
	while a != [1,1,1]:
		a[count%3] = (sum(a))%n
		if a[count%3] == 0:
			break
		count+=1
	if a == [1,1,1]:
		rounds +=1
		print n
	n+=2
	a = [1,1,3]
	count = 0

print 'Time Taken:', time.time() - start


"""
2009
Time Taken: 2.71862387657

much easier than i expected... ._.;;
just find the 124th number to satisfy this. Since we're in a mod, we're bound to get repeating numbers so... yeah :x not very hard.

"""
