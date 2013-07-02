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
	temp_set = set()
	temp_sum = sum(setz)
	set_size = len(setz)
	works = True
	for i in xrange(1,set_size):
		if not works:
			break
		for j in combinations(sub_index[:set_size],i):
			k = sum( setz[(ord(l)-97)] for l in j)
			if k in temp_set:
				works = False
				break
			else:
				temp_set.add(k)
			if i * 2 > set_size and 2 * k < temp_sum:
				works = False
				break
			elif i *2 < set_size and k *2 > temp_sum:
				works = False
				break
	if works:
		sumz += temp_sum
		count += 1
		print temp_sum, index, count
		print "This set works:", setz

print sumz, count
print "Time Taken:", time.time() - start
