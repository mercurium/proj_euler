#NOTE TODO need to solve it
import time
START = time.time()
SIZE = 10**2

squares = set([x**2 for x in range(10**5)])

count = 0
for a in range(1,SIZE):
    oldCount = count
    for b in range(a, SIZE-a):
        cSq = a**2+b**2-1
        if cSq not in squares:
            continue
        c = int(cSq**.5)
        if a+b+c <= SIZE:
            print a,b,c
            count+=1
print count

print "Time Taken:", time.time() - START

"""
c^2 +1 = a^2+b^2
c^2 = b^2 + (a^2-1)
c = (b+k)
a^2-1 = 2bk+k^2
b = (a^2-1-k^2)/2k
c = (a^2-1+k^2)/2k

a+b+c = a+(a^2-1)/k

k = c-b
a = (2bk+k^2+1)^(1/2)
a+b+c = b+c+ (c^2 +b^2 +1)^.5


"""
