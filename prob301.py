import time
import math
start = time.time()

values = set([])
for i in range(1,2**16 +1): #<--- I tested this for small numbers..
  if i^(2*i)^(3*i) == 0:
    values.add(i)
#print values
print len(values)
print "Time elapsed = " + str(time.time()-start)

"""
by sheer luck and wikipedia powers.... I found out that the answer is merely the 31st fibonacci number... wat

I tested the answer for small and found out pretty quickly that it was just fib numbers.. and then i wrote like 2 lines of code to generate the 31st fibo number... didn't think it would work O___O

http://en.wikipedia.org/wiki/Game_of_Nim

To lose, you just need to have a xor b xor c be 0... rofl


"""




