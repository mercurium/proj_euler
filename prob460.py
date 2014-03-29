#NOTE TODO need to solve it
import time, random
START = time.time()
from math import *
SIZE = 100

minDist = SIZE if SIZE != 10**4 else 180.460086537
for k in range(20,300):
    break
    for h in range(2200,SIZE):
        velocity = (h-1)/log(h)
        dist = ((h-1)**2+k**2)**.5
        for k2 in range(min(5000,SIZE/2-k+1),1,-1):
            for h2 in range(h+SIZE/4,SIZE):
                velocity2 = h if h2==h else (h2-h)/(log(h2)-log(h))
                dist2 = ((h2-h)**2+k2**2)**.5
                totalDist = (SIZE-2.*k-2*k2)/h2 + dist/velocity * 2  +dist2/velocity2 * 2
                if totalDist < minDist:
                    minDist = totalDist
                    print h,h2,k,k2,minDist

for n in range(4,10):
    print n
    for iteration in range(10**6):
        hLst = [1]
        kLst = [0]
        for i in range(1,n+1):
            hLst.append(random.randint(2,SIZE))
            kLst.append(random.randint(max(0,min(kLst)-20),SIZE/2))
        #kLst = [0, 14, 352, 1070, 2535, 4034]
        #hLst = [1, 656, 1833, 3087, 4388, 4889]
        hLst.sort()
        kLst.sort()
        totalDist = (SIZE-2.*kLst[-1])/hLst[-1]
        for i in range(1,n+1):
            vel = hLst[i] if hLst[i]==hLst[i-1] else (hLst[i]-hLst[i-1])/(log(hLst[i])-log(hLst[i-1]))
            totalDist += 2*((hLst[i]-hLst[i-1])**2+(kLst[i]-kLst[i-1])**2)**.5 / vel
        if totalDist < minDist:
            minDist = totalDist
            print hLst, kLst,minDist

print "Time Taken:", time.time() - START


"""
1666 4640 2 499 18.8528104209
1666 4982 2 2537 18.5827906416
2276 5036 130 2738 18.5696552345
2200 3998 5363 86 1217 2904 18.5235163522
[1, 656, 1833, 3087, 4388, 4889] [0, 14, 352, 1070, 2535, 4034] 18.4512660003
is a hard limit on how big it can be.

[1, 11, 17, 26, 35, 46, 53] [0, 1, 3, 6, 13, 29, 47] 9.24596933422
[1, 11, 19, 23, 39, 45, 49] [0, 1, 4, 6, 19, 28, 43] 9.23781289606
[1, 12, 18, 23, 33, 40, 45, 49] [0, 1, 3, 5, 11, 18, 29, 46] 9.23538839065


[1, 3, 4, 5] [0, 1, 1, 2] 4 4.66818783436
"""
