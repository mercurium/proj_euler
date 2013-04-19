import time
start = time.time()
from bitarray import bitarray


size = 999966663333
limit = 999983
soft_lim = size
prime_set = set()
temp = bitarray('0' * (limit+5))
for i in range(3,len(temp),2):
  if temp[i] == 0:
    prime_set.add(i)
    for j in range(i**2,len(temp),2*i):
      temp[j] = 1

prime_lst = [2] + sorted(list(prime_set))
pl = prime_lst

count = 0
sumz = 0
for i in xrange(len(prime_lst)-1):
  if prime_lst[i+1]**2 > soft_lim: break
  #a = (pl[i+1]**2-1)//pl[i] - pl[i]
  #b = pl[i+1] - (pl[i]**2)//pl[i+1] -1
  
  a_n = pl[i+1]**2 // pl[i]
  a_sum = ( a_n  + 1 - (pl[i] + 1) ) * (a_n + (pl[i] +1) )//2
  
  b_m = pl[i]**2 // pl[i+1]
  b_sum = ( pl[i+1] - b_m -1) * (pl[i+1] + b_m)/2
  sumz += a_sum * pl[i] + b_sum * pl[i+1] - pl[i+1] * pl[i] * 2
  #count += a+b-2
  #debugging lines
  
print sumz
#print count

print "Time Taken:", time.time() - start

"""

~/Desktop/python_projects/proj_euler $python prob234.py
1259187438574927161
3764437
Time Taken: 0.75043296814

Main idea behind this problem is that the numbers that are divisible by a number are prime[i]**2+prime[i], prime[i]**2+2*prime[i]... etc, for divisible by prime[i], and then we can compute the numbers that are divisible by prime[i+1] in a similar fashion.

I technically already had the idea completely fleshed out at a previous point, but was too lazy to code up till now
"""

