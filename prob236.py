#NOTE TODO need to solve it
import time
START = time.time()

def gcd(a,b):
    while a != 0:
        a,b = b%a, a
    return b

A = [5248, 1312, 2624,5760,3936]
B = [640,1888,3776,3776,5664]

spoilRate = set()
for a in range(1,1312+1):
    for b in range(1,1888+1):
        x,y = 1888*a, 1312*b
        if x > y:
            continue
        x,y = x/gcd(x,y), y/gcd(x,y)
        spoilRate.add((x,y))

spoilRate1 = set()
for spoil in spoilRate:
    if 5248 > spoil[0]/gcd(spoil[0],5) and 640 > spoil[1]/gcd(spoil[1],41):
        spoilRate1.add(spoil)
print len(spoilRate), len(spoilRate1)


spoilRate2 = set()
for spoil in spoilRate1:
    if 5760 > spoil[0]/gcd(spoil[0],59) and 3776 > spoil[1]/gcd(spoil[1],90):
        spoilRate2.add(spoil)

print len(spoilRate), len(spoilRate1), len(spoilRate2)

for spoil in spoilRate:
    a,b = sum(A) * spoil[1], sum(B) * spoil[0]
    a,b = a/gcd(a,b), b/gcd(a,b)



print "Time Taken:", time.time() - START


"""
(x/1312)/(y/1888) = (1888x/1312y)
a/b = 1475/1476
59x/41y = p/q

41py = 59qx

x = 25
y = 36

(x/5248)/(y/640) = (640x/5248y)
5x/41y = p/q

5x/p = 41y/q


"""
