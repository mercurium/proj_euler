import time
start = time.time()

size = 10**4
divisor_sum = [0]*size

#For each number, add it to all numbers j that this index i is a factor of.
for i in xrange(1,size):
    for j in xrange(2*i,size,i):
        divisor_sum[j] += i

count = 0
sumz = 0
for i in xrange(1,size): #for each num, check if the conditions are satisfied...
    if divisor_sum[i] < size and divisor_sum[divisor_sum[i]] == i and divisor_sum[i] != i:
        count += 1
        sumz+= i
print sumz
print "Time Taken:", time.time() - START
