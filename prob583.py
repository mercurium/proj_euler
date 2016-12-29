#NOTE TODO need to solve it
import time
from primes import divisors
START = time.time()
SIZE  = 10**4


def isSquare(n):
    k = int(n**.5)
    return n == k**2 or n == (k+1)**2 or n == (k-1)**2

total = 0

for m in xrange(1,1000):
    print m
    for n in xrange(1,m):
        h1 = m**2 - n**2
        w  = 2*m*n
        d2 = m**2 + n**2

        if h1*2 + w*2 > SIZE:
            break

        for i in xrange(2):
            if w % 4 != 0:
                h1, w = w,h1
                continue
            for a in divisors(w/4):
                for c in divisors(w/ (4*a)):
                    b = w / (4*a * c)
                    if a <= b:
                        break
                    h2 = (a**2 - b**2) * c
                    d1 = (a**2 + b**2) * c

                    if h2 > h1:
                        continue

                    if isSquare((h1+h2)**2 + (w/2)**2):
                        print "AB:", h1, "BD:", w, "BC:", d1, "Mult:", c
                        if (h1*2 + w + d1*2) <= SIZE:
                            total += h1*2 + w + d1 * 2


            for c in divisors(w/ 2):
                for k in divisors(w/(2*c)):
                    aTemp = w / (2*k) + k
                    if aTemp % 2 == 1 or aTemp/2 < k:
                        continue
                    a = aTemp / 2
                    b = a - k
                    h2 = 2*a*b* c
                    d1 = (a**2 + b**2) * c

                    if h2 > h1:
                        continue

                    if isSquare((h1+h2)**2 + (w/2)**2):
                        print "AB:", h1, "BD:", w, "BC:", d1, "Mult:", c
                        if (h1*2 + w + d1*2) <= SIZE:
                            total += h1*2 + w + d1 * 2

            h1,w = w, h1



print total
print "Time Taken:", time.time() - START


"""
Rectangle = ABDE
Flap      = BCD

h1 = AB = DE = height of envelope
w  = AE = BD = width of envelope

h2 = height of flap

(w/2)^2 + h2^2 = int squared      ( this is BC and CD) d3
(w/2)^2 + (h1+h2)^2 = int squared ( this is AC and CE) d2
w^2 + h1^2 = int squared          ( this is AD and BE) d1

BD = AE -> integer already



h1 = m^2 - n^2
w  = 2mn
d1 = m^2 + n^2



"""
