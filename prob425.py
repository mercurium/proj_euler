import time
start = time.time()
import Queue
size = 10**5

prime_lst = [2]
tmp = [1,1,0] + [0,1]*(size//2 -1)

for i in xrange(3,len(tmp),2):
	if tmp[i] == 0:
		for j in xrange(i**2,len(tmp),2*i):
			tmp[j] = 1
		prime_lst.append(i)
prime_set = set(prime_lst)

relatives = {2,3,5,7}
reachable = {2:2,3:3,5:5,7:7}
reach_lst = Queue.PriorityQueue(len(prime_set))

reach_lst.put(2)
reach_lst.put(3)
reach_lst.put(5)
reach_lst.put(7)

while not reach_lst.empty(): 
	next_number= reach_lst.get()
	len_next_number= len(str(next_number))
	for digit in xrange(0,len_next_number+ 1):
		num2 = (next_number/ 10 ** (digit + 1)) * 10 ** (digit + 1) + next_number% 10 ** digit
		val = 10 ** digit
		for dig_check in xrange(10):
			if num2 in prime_set and num2 not in relatives:
				if num2 not in reachable:
					reachable[num2] = max(num2,reachable[next_number])
					reach_lst.put(num2)
					if num2 >= reachable[num2]:
						relatives.add(num2)
			num2+=val


print sum(prime_lst) - sum(relatives)
print "Time Taken:", time.time() - start
