import time
start = time.time()

size = 10**9
minz = 1 #lst[0] has cost 1 right now, minz = cost of encoding lst[0]
lst = [1,0,0,1] #encoding 2 items, one of cost 1, one of cost 4
while sum(lst) +lst[0] < size: #transforming k -> (k+1) and (k+4)
    a = lst.pop(0) 
    lst[0] += a # adding (k+1)
    lst.append(a) # adding (k+4)
    minz += 1 #we're incrementing what lst[0] costs.
total = sum(lst)
b = size - total  #we're not at the goal yet so we need to increment more
lst[0] -= b       #but only partially since we don't need all of them.
lst[1] += b
lst.append(b)

print minz
print lst, sum(lst)
total_sum = size * minz
for i in xrange(len(lst)):
    total_sum += i * lst[i]

print total_sum
print "Time Taken:", time.time() - start

"""
~/Desktop/python_projects/proj_euler $python prob219.py
63
[306548149, 190302805, 188941273, 260791401, 53416372] 1000000000
64564225042
Time Taken: 9.29832458496e-05

Interesting thing to note for this problem is that if you have a solution of size (n-1), which has the smallest encoding of size k, then your solution of size n will have the same thing as the solution for size (n-1) except that encoded item of size k will now be two items, one of size (k+1), the other of (k+4). 

Reasoning for this is because at each stage, in order to add a new encoding, we need to change one encoding into two. This process makes a cost of k into (k+1) and (k+4). Since we want the minimum cost, and we're effectively adding (k+5) to our total cost, we want the k that we replace to be as small as possible. Thus we replace the smallest encoding from the previous step with two new items.

Now for the algorithm. If we're replacing k with (k+1) and (k+4), but there's say 30 items of cost k, and we have >30 steps, we know that in the next 30 steps, we're going to be transforming all of those k items into new items. Thus, there's no need to do it one at a time. We should transform them all at once, which makes the cost much cheaper.

Yep :). This was a cool problem :D
"""
