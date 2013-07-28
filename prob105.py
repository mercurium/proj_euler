import time
start = time.time()
import string
from itertools import combinations

data = open('sets.txt', 'r')
data = data.read()
subsets = string.split(data.strip(), '\n')
for i in xrange(len(subsets)):
	subsets[i] = [int(x) for x in string.split(subsets[i],',')]

sub_index = 'abcdefghijklmno'

print len(subsets)
sumz = 0
count = 0
for index in range(len(subsets)):
	setz = subsets[index]
	subset_sums = set()
	TEMP_SUM = sum(setz)
	SET_SIZE = len(setz)
	works = True
	for i in xrange(1,SET_SIZE):
		if not works:
			break
		temp_set = set()
		for j in combinations(sub_index[:SET_SIZE],i):
			k = sum( setz[(ord(l)-97)] for l in j)
			if k in subset_sums or k in temp_set:
				works = False
				break
			elif len(subset_sums) >= 1 and k < max(subset_sums):
				works = False
				break
			else:
				temp_set.add(k)
		for val in temp_set:
			subset_sums.add(val)	
	if works:
		sumz += TEMP_SUM
		count += 1
		print temp_sum, index, count, sumz
		print "This set works:", setz
		print TEMP_SUM, index, count, sumz

print sumz, count
print "Time Taken:", time.time() - start

"""
Congratulations, the answer you gave to problem 105 is correct.

You are the 3559th person to have solved this problem.

Return to Problems page.

"""
