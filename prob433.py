#NOTE TODO need to solve it
import time
start = time.time()

count = 0
size = 100

vals = dict()

def euclid(a, b): #returns c,d such that ac+bd =1
    if b == 0:
        return 0
    count = 0
    while b != 0:
        count, a,b = count+1,b, a%b
    return count
ext_gcd = euclid

for i in xrange(1,size+ 1):
    for j in xrange(1,i):
        count += 2*ext_gcd(i,j)+1


count += size # This is for i = j

print count

print "Time Taken", time.time() - start

"""

OH YEAHHHH.... I forgot. I wrote this one using C++ since it was taking so long with python.... :D;;;


"""
