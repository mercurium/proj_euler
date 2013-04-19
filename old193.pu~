import time
start = time.time()
from bitarray import bitarray

size = 17
temp = bitarray('0'*(size+1))

size_sq = size**2
number = size_sq*3/4 + size_sq%2
print 2, number

for i in xrange(3,size+1,2):
  if temp[i] == 0:
    if i**2 * 2 > size_sq:
      number -=1
    else:
      number = number - int(number/i**2.)
  	
    for j in xrange(3*i,size+1,2*i):
      temp[j] = 1
    print i, number

print number
print "Time Taken:", time.time()-start



items = [2,3,5,7,11,13,17,19,23,29]
#test number 3
total_sq = 0
for i in range(1,size):
  total_sq+= int((size_sq/i**2)**.5)

print size_sq - total_sq

#test number 2
items = [2,3,5,7,11,13,17,19,23,29]
stuff_left = set(range(1,size**2+1))
new_items = set()

for num in items:
  for item in stuff_left:
    if item%(num**2) == 0:
      new_items.add(item)
  print num, size**2 - len(new_items)

print "Time Taken:", time.time()-start


"""
#test number 1
primes = [2,3,5,7,11,13,17,19,23,29]

count = 0
for i in range(1,size**2):
  add = True
  for j in primes:
    if i% j**2 == 0:
      add = False
  if add: count +=1


print "Count is:", count

print "Time Taken:", time.time()-start

"""

"""
~/Desktop/python_projects/proj_euler $python prob193.py
0.607927102847
6.84465068462e+14
Time Taken: 20.8167331219

"""
