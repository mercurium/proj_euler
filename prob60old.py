#note to self, if p1 and p2 can concatenate together, then either one of them is 3 or p1 = p2 mod 3 (or else we get 1+2 = 0 mod 3 --> 3|p1p2)

import time
start = time.time()
from primes import * 


primesss = set()
size = 10**7
primes_uns = [0]*size
for i in range(2,len(primes_uns)):
  if primes_uns[i] == 0:
    for j in range(2*i,len(primes_uns),i):
      primes_uns[j] += 1
    primesss.add(i)

temp = list(primesss)
temp.sort()
prime_s = temp[:3000]
items = dict()

def is_primez(n):
  if n <= size: return n in primesss
  val = m_r(n)
  if val != -1: return val
  return is_prime(n)

print "part0 done"
print "Time Taken: " + str(time.time()-start)

for i in prime_s:
  items[i] = set()

lst1 = [3] + [x for x in prime_s if x%3 ==1]
lst2 = [3] + [x for x in prime_s if x%3 ==2]
for i in lst1: #first loop lol
  for j in lst1:
    if is_primez(int(str(i) + str(j)) ) and is_primez(int(str(j) + str(i)) ):
      items[i].add(j)
      items[j].add(i)

for i in lst2: #first loop lol
  for j in lst2:
    if is_primez(int(str(i) + str(j)) ) and is_primez(int(str(j) + str(i)) ):
      items[i].add(j)
      items[j].add(i)

print items
print "part1 done"
print "Time Taken: " + str(time.time()-start)
items2 = dict()

for i in items.keys():
  if len(items[i]) >= 2:
    for j in items.keys():
      if i< j and i in items[j] and j in items[i]:
        stuff = items[i].intersection(items[j])
        if len(stuff) >= 2:
         items2[(i,j)] = items[i].intersection(items[j])

print items2
print "part2 done"
print "Time Taken: " + str(time.time()-start)

items3 = dict()

for i in items2.keys():
  for j in items2.keys():
    it = set(list(i)+list(j))
    if len(it) == 4 and i[0] in items2[j] and i[1] in items2[j] and j[0] in items2[i] and j[1] in items2[i]:
      stuff = items2[i].intersection(items2[j])
      if len(stuff) != 0:
        items3[tuple(it)] = stuff

print items3
print "part3 done"
print "Time Taken: " + str(time.time()-start)




