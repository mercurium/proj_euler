import time
START = time.time()
SIZE = 10**6

def findTrailing(num):
    if num % 10 == 0:
        return 0
    ans = 0
    for i in range(100):
        if pow(num,i,100) == i:
            ans = i
            break
    if ans == 0:
        print num
        return 0
    for i in range(3,10):
        ans = pow(num,ans,10**i)
    return ans

sumz = 0
for i in range(2,SIZE+1):
    sumz += findTrailing(i)
print sumz
print "Time Taken:", time.time() - START

"""
This problem abuses the fact that n^x = x mod 10^9 means that n^x = x mod 10^(2,3,4,5,6,7,8,9)
Similarly, since n^(2*10^(k-1)) = 1 mod 10^k, if n^x = x mod 10^k and n^x = y mod 10^(k+1), then n^y = y mod 10^(k+1)


18:44 ~/Desktop/python_projects/proj_euler $ python prob455.py 
450186511399999
Time Taken: 18.9543330669


Congratulations, the answer you gave to problem 455 is correct.

You are the 26th person to have solved this problem.

"""
