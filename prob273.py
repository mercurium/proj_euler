import time
start = time.time()
from itertools import combinations

nums = [5,13,17,29,37,41,53,61,73,89,97,101,109,113,137,149]
numbers = {5:(1,2),13:(2,3),17:(1,4),29:(2,5),37:(1,6),41:(4,5),53:(2,7),61:(5,6),73:(3,8),89:(5,8),97:(4,9),101:(1,10),109:(3,10),113:(7,8),137:(4,11),149:(7,10)}

numbs = [(1,2),(2,3),(1,4),(2,5),(1,6),(4,5),(2,7),(5,6),(3,8),(5,8),(4,9),(1,10),(3,10),(7,8),(4,11),(7,10)]

def transform(p1,p2):
	a,b = p1
	c,d = p2
	pair1 = (a*c+b*d,abs(a*d-b*c))
	pair2 = (a*d+b*c,abs(a*c-b*d))
	return pair1,pair2



def main():
	sumz = 0
	old_set = set([(0,1)])
	new_set = set()
	for i in numbs:
		print i
		for j in old_set:
			new_set.add(j)
			new1,new2 = transform(i,j)
			if j != (0,1):
				new_set.add(new1)
			new_set.add(new2)
		old_set = new_set
		new_set = set()
	return old_set

values = main()
print len(values)
a = sum(min(x) for x in values)
print a 

print "Time Taken:", time.time()-start


"""


(a^2+b^2)(c^2+d^2) = (ac-bd)^2+(ad+bc)^2
                   = (ac+bd)^2+(ad-bc)^2
(from http://en.wikipedia.org/wiki/Brahmagupta%E2%80%93Fibonacci_identity )

5 13 17 29 37 41 53 61 73 89 97 101 109 113 137 149
are the numbers of the form 4k+1 < 150

5 1 2
13 2 3
17 1 4
29 2 5
37 1 6
41 4 5
53 2 7
61 5 6
73 3 8
89 5 8
97 4 9
101 1 10
109 3 10
113 7 8
137 4 11
149 7 10

2032447591196869022
Time Taken: 31.8353140354
(also took like... 3 gb)

So what I did was, at each step, we add on another factor. It can either be used or not used, and if it's used, it can be used in one of two ways. So... yeah :D 21,523,361 different square pairs were used... so big... much more than expected...
"""
