import time
START = time.time()
from bitarray import bitarray

SIZE = 50000
lim = 12000

plst = range(SIZE)
plst[2] = 2
for i in xrange(2,len(plst)):
	if plst[i] == i:
		for j in xrange(i*i,len(plst),i):
			plst[j] = i

def factor(n):
	if n == plst[n]:
		return [n]
	factors = []
	while n != 1:
		factors.append(plst[n])
		n /= plst[n]
	return sorted(factors)

def divisors(n):
	factors = factor(n)
	divisors = set([1])
	new_divs = set()
	for i in xrange(0,len(factors)):
		for val in divisors:
			new_divs.add(val)
			new_divs.add(val * factors[i])
		divisors = new_divs
		new_divs = set()
	divisors.remove(1)
	return sorted(list(divisors))

def possible_divisor_sums(n):
	divs = divisors(n)
	def helper(prod, index, count, sum_val):
		if prod == n:
			return [(count,sum_val)]
		if index == len(divs) or prod * divs[index] > n:
			return []
		ans1 = helper(prod,index+1,count,sum_val)
		ans2 = [] if n %(prod * divs[index]) != 0 else helper(prod*divs[index],index,count+1,sum_val + divs[index])
		return ans1+ans2
	return helper(1,0,0,0)
pds = possible_divisor_sums

solution = [-1] * (lim +1)

for i in xrange(2,SIZE):
	answers = pds(i)
	for ans in answers:
		count = ans[0] + i - ans[1]
		if count <= lim and solution[count] == -1:
			solution[count] = i
	if -1 not in solution[1:]:
		break

uniq_solution = set()
for i in xrange(2,lim):
	uniq_solution.add(solution[i])

print sum(uniq_solution)
print "Time Taken:", time.time() - START


"""
Congratulations, the answer you gave to problem 88 is correct.

You are the 4181st person to have solved this problem.

01:39 ~/Desktop/python_projects/proj_euler $ python prob88.py 
7587457
Time Taken: 2.56992316246

Okay, so this isn't really that hard of a problem to solve. What you should do is, for each number, get the possible sums of the products of divisors, and then add on (number - (sum of divisors)) 1's back on. This gives the count. This isn't hard to do, but it's annoying to count how many possible divisor products you can get. The only reason I have this working is because I got tested on this for a linked in interview LOL...

"""
