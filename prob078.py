import time
START = time.time()

size = 10**6
partCount = {0:1,1:1,2:2,3:3,4:5}

def partitions(n):
    if n in partCount:
        return partCount[n]
    sumz = 0
    k = 1
    while (n-(k*(3*k-1)/2)) >= 0:
        sumz+= (-1)**(k%2-1)* partCount[(n- k*(3*k-1)/2)]
        k+=1
        
    k = -1
    while (n-(k*(3*k-1)/2)) >= 0:
        sumz+= (-1)**(k%2-1)* partCount[(n- k*(3*k-1)/2)]
        k-=1
    partCount[n] = sumz %10**6
    return partCount[n]
    

part = 1
i = 4
while part % size != 0:
    i+=1
    part = partitions(i)
print "The answer is:", i
print "Time Taken:", time.time() - START






"""
so... reoutlining the program because god damn i don't remember it...

P(n) = P(n-1) + \sum_{k=1}^n P(n-k,k)


What I'm doing wrong atm is that I'm running out of space... and then the thing has to rehash... so hm. I need to make it so that it's O(n) space rather than O(n^2)... otherwise my computer is going to complain at me.

http://en.wikipedia.org/wiki/Partition_(number_theory)#Partition_function_formulas

...wat
wtf?

Answer = 55374... T.T;;; I wasn't able to compute the number of partitions quickly on my own
"""







