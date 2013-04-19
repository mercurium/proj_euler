import time
start = time.time()


size =  4*10**7
prime_set = set()
totient_val = [x for x in range(size+1)]
for i in xrange(2,size):
  if totient_val[i] == i:
    for j in xrange(i,size,i):
      totient_val[j] = (i-1)*totient_val[j]/i
    prime_set.add(i)
  totient_val[i] = int(totient_val[i])
totient_count = [0] * (size+1)

print "Time Taken:", time.time() - start

for i in xrange(2,size):
  totient_count[i] = totient_count[totient_val[i]] +1


print "Time Taken:", time.time() - start
sumz = 0
for i in prime_set:
  if totient_count[i] == 24: sumz += i

print sumz

print "Time Taken:", time.time() - start


"""~/Desktop/python_projects/proj_euler $python -i prob214.py
Time Taken: 63.1803610325
Time Taken: 74.8065619469
1677366278943
Time Taken: 75.3312809467
...I am not proud of this code... T_T
"""

