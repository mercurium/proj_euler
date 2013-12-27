import time
START = time.time()

combinations = [1,0,1]
for i in xrange(30):
	combinations.append(combinations[-2] + combinations[-3])

s = [""]*33
s[2] = "2",
s[3] = "3",

for i in range(4,33):
	s[i] = ["2" + x for x in s[i-2]] + ["3" + x for x in s[i-3]]
	#s[i].sort()

count = [1] * len(s[32])
new_count = [0] * len(count)

lst = []
for x in s[32]:
	new_lst = [int(i) for i in x]
	lst.append( set(  [sum(new_lst[:j+1]) for j in range(len(new_lst) -1 ) ]))

compat = set()

for i in range(len(count)):
	if count[i] == 0:
		continue
	for j in range(len(new_count)):
		intersect = False
		for k in lst[i]:
			if k in lst[j]:
				intersect = True
				break
		if not intersect:
			new_count[j] += count[i]
			compat.add((i,j))

count = new_count[:]
new_count = [0]*len(count)
print "finished iteration:", i, "count is at:", sum(count)

for i in range(8):
	for val in compat:
		new_count[val[1]] += count[val[0]]
	count = new_count[:]
	new_count = [0]*len(count)
	print "finished iteration:", i, "count is at:", sum(count)


print sum(count)
print "Time Taken:", time.time() - START





"""
Okay, I should really optimize this one, but... solved it xD. This is pretty much just a check at each stage to see if a certain configuration is compatible with the one above. If it is, then we're good, otherwise no. Repeat 10x to get answer.

Congratulations, the answer you gave to problem 215 is correct.

You are the 2133rd person to have solved this problem.


~/proj_euler $python prob215.py 
finished iteration: 0 count is at: 37120
finished iteration: 1 count is at: 592050
finished iteration: 2 count is at: 10178548
finished iteration: 3 count is at: 199541122
finished iteration: 4 count is at: 3919649942
finished iteration: 5 count is at: 83141220006
finished iteration: 6 count is at: 1722438038790
finished iteration: 7 count is at: 37941687807654
finished iteration: 8 count is at: 806844323190414
806844323190414
Time Taken: 7.09183692932

"""
