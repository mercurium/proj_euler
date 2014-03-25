import time
START = time.time()

sumz = 0
for i in range(3,1001):
    if i%2 == 0:
        sumz += i*i-2*i
    else:
        sumz += i*i-i
print sumz


print "Time Taken:", time.time- START


"""
For odd numbers, turns out the remainder is n^2-n, and for even numbers, it's n^2-2n. Lol, who knew.

"""
