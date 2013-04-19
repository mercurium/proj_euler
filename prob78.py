import time
start = time.time()

size = 10**6
vals = {0:1,1:1,2:2,3:3,4:5}

def partitions(n):
  if n in vals:
    return vals[n]
  sumz = 0
  k = 1
  while (n-(k*(3*k-1)/2)) >= 0:
    sumz+= (-1)**(k%2-1)* vals[(n- k*(3*k-1)/2)]
    k+=1
    
  k = -1
  while (n-(k*(3*k-1)/2)) >= 0:
    sumz+= (-1)**(k%2-1)* vals[(n- k*(3*k-1)/2)]
    k-=1
  vals[n] = sumz %10**6
  return vals[n]
  

part = 1
i = 4
while part % size != 0:
  i+=1
  part = partitions(i)
  print i
print i, "DONE!!! :D :D :D"
print "Time Taken: " + str(time.time()-start)

for i in range(1,10):
  print i, vals[i]

#19, 74, 449, 599
#P(n) = sum(P(n,k) for k = 1 to n) = P(n-1) + sum(P(n-k,k) for k = 1 to n)


"""
so... reoutlining the program because god damn i don't remember it...

P(n) = P(n-1) + \sum_{k=1}^n P(n-k,k)


What I'm doing wrong atm is that I'm running out of space... and then the thing has to rehash... so hm. I need to make it so that it's O(n) space rather than O(n^2)... otherwise my computer is going to complain at me.

http://en.wikipedia.org/wiki/Partition_(number_theory)#Partition_function_formulas

...wat
wtf?

Answer = 55374... T.T;;; I wasn't able to compute the number of partitions quickly on my own
"""







