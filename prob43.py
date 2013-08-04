import time
start = time.time()
from itertools import permutations as perm
import string

lst = perm(['1','2','3','4','5','6','7','8','9','0'],10)
items = set()
#we check in the order of numbers with dig 456 divisible by 5 first since it eliminates 80% of the numbers. We can also check it based on the last digit and without wasting time converting it to an int.

#by not converting "n[5] in '05' " to "int(n[5])%5 == 0", we shave the running time from 6.17 seconds to 3.77
#doing the same for "n[3] in '02468' " vs "int(n[3])%2 == 0, we go from 4.424 to 3.772, saving us .652 seconds, or cutting running time down by 14.7% 

for item in lst:
  n = string.join(item, '') #1-3,2-5,3-6,4-7,5-8
  if n[5] in '05' and n[3] in '02468' and int(n[2:5])%3 == 0 and int(n[4:7])%7 ==0 and int(n[5:8])%11==0 and int(n[6:9])%13 == 0 and int(n[7:10])%17 == 0:
    items.add(int(n))
print sum(items)
print items
print "Time taken:",time.time() -start
