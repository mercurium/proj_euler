import time
START = time.time()

def rot(a,b):
    a = sorted(str(a))
    b = sorted(str(b))
    return a == b


for i in range(100000,300000):
    if rot(i,2*i) and rot(i,3*i) and rot(i,4*i) and rot(i,5*i) and rot(i,6*i):
        print [i*x for x in range(1,7)]
        break

print "Time Taken:", time.time() - START
