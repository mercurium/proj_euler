#NOTE TODO need to solve it
import time
start = time.time()

mult = 10**15
size = 10**9
count = 0
num1,num2 = 1,1
set_to_check = set()
set_to_check2 = set()

for i in xrange(1,10**6):
  if mult/(i* size) != mult/(size*i+num1):
    print i
    count +=1
    set_to_check.add(i)

print '\n', count
print "Time Taken: ", time.time()-start


for i in xrange(1,10**6):
  if mult/(i* size) != mult/(size*i+num2):
    print i
    count +=1
    set_to_check2.add(i)

print '\n', count
print "Time Taken: ", time.time()-start



"""
m = multiplicative factor,  10^15
s = size that we mod by, 10^9
n = 10^6, largest int n where n * s <= m. 10^6 for set values
a = adjusted n when we have adjusted s.
R = number that we multiply s by, when we get our position/10^9


ALL INTS

variables to find:
n, a 


Given:
R, s, k

m >= R*s*n
m >= (R*s+k)(n-a)

We want to find when a = 0, given R,s, k. Should be easy...









"""
