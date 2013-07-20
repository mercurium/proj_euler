import string
import math
import time
start = time.time()

def rep_sq(n, powz, mod):
        if powz == 0: return 1
        if powz == 1: return n % mod 
    
      
        val = int(math.log(powz,2))
        lst = [1,n] + [0] * val 
        for i in range(2,len(lst)):
                lst[i] = lst[i-1]**2 % mod 
      
        pows = [0] * (val+1)
        power = powz
        for i in range(0,len(pows)):
                pows[i] = power % 2 
                power = power //2 
        product = 1 
        for i in range(0,len(pows)):
                if pows[i] == 1:
                        product = product * lst[i+1] % mod 
        return product

vals = (1,1,2)

a = (5**.5+1)/2

def find_R(n):
	return 0
 
print "Time Taken: ", time.time()-start


"""
vals = (1,1,2)
count = 4
for i in xrange(500000):
  vals = (vals[1],vals[2],vals[1]+vals[2])
  val = (string.join(sorted(str(vals[2])[:9]), '') == '123456789', string.join(  sorted(  str(vals[2])[-9:]  ), '') == '123456789')
  if val == (True,True):
    print i+count
    break
  if val[0] == True:
    print "Front of ", i+count, "is pan"
  if val[1] == True:
    print "Back of ", i+count, "is pan"
    
print "Time Taken: ", time.time()-start


okay, so using that one technique I learned about, this could be feasible... o.o... now to figure out how to deal with it :D;;;
"""
