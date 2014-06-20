import time
from bitarray import bitarray
START = time.time()

SIZE = 10**9*2
sq1 = bitarray(SIZE+1)
sq2 = bitarray(SIZE+1)
sq3 = bitarray(SIZE+1)
sq7 = bitarray(SIZE+1)
sq1[:] = False
sq2[:] = False
sq3[:] = False
sq7[:] = False
print "Time Taken:", time.time() - START

for a in xrange(1,int(SIZE**.5)+10): #0,1,2 mod 4
    diff = 1 if a %4 == 0 else 4
    for b in xrange(1,SIZE,diff):
        if a**2 + b**2 <= SIZE:
            sq1[a**2+b**2] = 1
        else:
            break
print "Time Taken:", time.time() - START

for a in xrange(1,int(SIZE**.5)+10):
    for b in xrange(2,SIZE,2):
        if a**2 + 2*b**2 <= SIZE:
            sq2[a**2+2*b**2] = 1
        else:
            break
print "Time Taken:", time.time() - START

for b in xrange(1,int((SIZE/3)**.5+10)):
    diff = 4 if b %4 != 0 else 1
    for a in xrange(max(1,b%4), SIZE,diff):
        if a**2 + 3*b**2 <= SIZE:
            sq3[a**2+3*b**2] = 1
        else:
            break
print "Time Taken:", time.time() - START

count = 0
for b in xrange(1,int((SIZE/7)**.5+10)):
    if b%4 == 2: continue
    diff = 4 if b %4 != 0 else 1
    start = (4-b)%4 if b%4 != 0 else 1
    for a in xrange(start, SIZE,diff):
        n = a**2+7*b**2
        if n <= SIZE:
            if sq1[n] == 1 and sq2[n] == 1 and sq3[n] == 1 and sq7[n] == 0:
                count +=1
                sq7[n] = 1
        else:
            break

print count
print "Time Taken:", time.time() - START

"""
Congratulations, the answer you gave to problem 229 is correct.

You are the 887th person to have solved this problem.
11325263
Time Taken: 1313.82633209 
need to do better for time though...

"""

