import time
START = time.time()
SIZE = 10**6

parent = range(SIZE)
num_child = [1] *  SIZE
next_call = [ (10**5+3 - (2*10**5+3)*k + (3*10**5+7)*k**3)%(10**6) for k in range(1,56)]
child = dict()

def gen_next_call():
	next_call.append( (next_call[-24] + next_call[-55]) %(10**6))
	next_call.append( (next_call[-24] + next_call[-55]) %(10**6))
	a = next_call.pop(0)
	b = next_call.pop(0)
	return a,b

count = 0
while True:
	if num_child[parent[524287]] >= 990000:
		break
	a,b = gen_next_call()
	if a == b: #This person called themself, misdial.
		continue
	count +=1
	if parent[a] == parent[b]: #person a called person b but they were already friends.
		continue
	if num_child[parent[a]] < num_child[parent[b]]: #We want to merge the smaller group into the bigger group
		a,b = b,a
	if num_child[parent[b]] == 1:
		num_child[parent[a]] +=1
		num_child[b] = 0
		parent[b] = parent[a]
		if parent[a] in child:
			child[parent[a]].append(b)
		else:
			child[a] = [a,b]
	else:
		num_child[parent[a]] += num_child[parent[b]]
		num_child[parent[b]] = 0
		for newChild in child[parent[b]]: #add the smaller group to the larger group
			child[parent[a]].append(newChild)
		oldParent = parent[b]
		for i in child[parent[b]]: #record that the parents of the smaller group have changed
			parent[i] = parent[a]
		del child[oldParent] #remove previous entry from the hash table to save space.
	if count % 1024 == 0 or (num_child[parent[a]] > 10000 and count %128 == 0):
		print count, num_child[parent[a]], len(child)

print count, num_child[parent[524287]], len(child)
print "The answer is:", count

print "Time Taken:", time.time() - START


"""
For this problem, I kept track of each of the clusters in a group, and whenever two people who weren't friends called each other, I merged them into one group. For each group, there would be one arbitrary person deemed to be the "parent", just so that it would be one person that each person in the group (including the parent) they could point to in order to uniquely identify the group.


Congratulations, the answer you gave to problem 186 is correct.

You are the 1541st person to have solved this problem.


The answer is: 2325629
Time Taken: 6.50162982941

"""
