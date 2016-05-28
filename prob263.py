#NOTE TODO need to solve it
import time
start = time.time()

SIZE = 10**6

def get_plst(size):
	lst = range(size+1)
	lst[0] = 1
	for i in xrange(2,len(lst),2):
		lst[i] = 2
	for i in xrange(3,len(lst),2):
		if lst[i] == i:
			for j in xrange(i**2,len(lst),2*i):
				lst[j] = i
	return lst

plst = get_plst(SIZE)

def pfactor(n):
	factors = []
	while n > 1:
		factors += [plst[n]]
		n /= plst[n]
	return sorted(factors)

def get_divisors(n):
	factors = pfactor(n)
	divisors = set([1])
	for f in factors:
		new_set = set()
		for d in divisors:
			new_set.add(f*d)
		for i in new_set:
			divisors.add(i)

	return sorted(list(divisors))

# This function is currently very slow for numbers with lots of factors =/
def practical_check(n):
	divs = get_divisors(n)
	div_sums = set([0])
	for val in divs:
		new_set = set()
		for i in div_sums:
			new_set.add(val+i)
		for i in new_set:
			div_sums.add(i)
	div_sums = sorted(list(div_sums))[:n+1]
	print "On item:", n, "Time up to now:", time.time() - start
	return div_sums == range(n+1)
pc = practical_check


items = []
for i in xrange(21,SIZE-18,2):
	if plst[i] == i and plst[i+6] == i+6 and \
	plst[i+12] == i+12 and plst[i+18] == i+18:
		items += [i+9]
		#print i,i+6,i+12,i+18

print "Out of", SIZE, "items, there were", len(items), "which were prime-triples"

sumz = 0
count = 0
for item in items:
	n = item
	if pc(n-8) and pc(n-4) and pc(n+4) and pc(n+8) and pc(n):
		count +=1
		sumz +=item
		print item
	if count == 4:
		break

print sumz
print "Time Taken:", time.time() - start



"""
These are some of the sets of 5 practical numbers
8 12 16 20 24
12 16 20 24 28
16 20 24 28 32
20 24 28 32 36
24 28 32 36 40
96 100 104 108 112
192 196 200 204 208
608 612 616 620 624
1472 1476 1480 1484 1488
2544 2548 2552 2556 2560
4088 4092 4096 4100 4104
8528 8532 8536 8540 8544
15088 15092 15096 15100 15104


"""
