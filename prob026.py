import time
START = time.time()


def rep_dig(n):
    if n == 1:
        return 0
    j = 10
    num_repeat = 1
    while j%n != 1:
        j*= 10
        num_repeat+=1
    return num_repeat
    
            
largest_sol = 0
largest_denom = 0
for i in xrange(999,2,-2): #Start at the biggest point, then work your way down while you can.
    if i < largest_sol:
        break
    if i%2!=0 and i%5 != 0: #the rep_dig method can't handle multiples of 2 or 5.
        num_repeat = rep_dig(i)
        if largest_sol < num_repeat:
            largest_sol = num_repeat
            largest_denom = i
print largest_denom, largest_sol

print "Time Taken:", time.time() - START


"""
If we have 10^k = 1 mod n, then that's the same as saying 10^2k = 1 mod n, etc, 
which means that the cycle repeats itself after this point. 
In other words, we just need to find the smallest number such that 10^k = 1 mod n
Strictly speaking, if n % 2, n%3, n%5 is not 0 for any of those, then k is a divisor of phi(n) 
(by a generalization of Fermat's Little Theorem). However, this is an unnecessary optimization for 
small numbers with d < 1000.

03:29 ~/Desktop/python_projects/proj_euler $ python prob26.py 
983 982
Time Taken: 0.0018401145935
"""
