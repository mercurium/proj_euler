import time
start = time.time()
import math

size = 10**9
sumz = 0

for m in range(1,int(math.sqrt(size/2))):
  diff = 2 if m%2==0 else 1
  for n in range(1,m,diff):
    a,b,c = 2*(m**2-n**2),4*m*n,m**2+n**2
    if a+2*c > size: break
    
    if c-b == 1 or c-b == -1:
      sumz+= b+2*c
      print a/2,b/2,c, 'b'
      
      
    elif c-a == 1 or c-a == -1:
      sumz+=a+2*c
      print b/2,a/2,c, 'a'
  if 2*m*(m+1) > size: break

print sumz
print "Time Taken:", time.time()- start
"""
518408346
Time Taken: 77.2402789593

Used the generic
a,b,c = m^2-n^2,2mn,m^2+n^2 and find sets where
2a = c+-1 or
2b = c+-1

Was going to use the fact that answers seem to be ~3.5x apart from each other (given answer, multiply by ~3.5 to get next answer)


4 3 5 a
15 8 17 b
56 33 65 a
209 120 241 b
780 451 901 a
2911 1680 3361 b
10864 6273 12545 a
40545 23408 46817 b
151316 87363 174725 a
564719 326040 652081 b
2107560 1216801 2433601 a
7865521 4541160 9082321 b
29354524 16947843 33895685 a
109552575 63250208 126500417 b
could use this info to make it run faster... :D
"""

