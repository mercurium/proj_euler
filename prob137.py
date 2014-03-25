import time
START = time.time()

values = [2,15]
mult = 13/2.
for i in xrange(1,14):
    val = values[-1]
    num = int(val * mult)
    while True:
        a = 5*num**2 + num * 2 + 1
        if int(a**.5)**2 == a:
            values.append(num)
            mult = (values[-1]-1.)/(values[-2])
            print num, values[-1]/(1.0*values[-2])
            break
        num+=1

print num
print "Time Taken:", time.time() - START
"""
I just need to find the 15th solution where 5n^2+2n+1 is a square...

First solution is n = 2
10th solution is n = 10
2,15,104,714,4895,33552,229970,1576239
"""
