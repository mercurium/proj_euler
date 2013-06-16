import time
start = time.time()
from bitarray import bitarray

size = 2**15
temp = bitarray('0'*(size+1))

size_sq = size**2
num_sq = 0

for i in xrange(1,size+1):
  if temp[i] == 0:
    num_sq += int((size_sq/i)**.5)
    print i, size_sq - num_sq
  if i**2 <= size:
      temp[i**2] = 1

print size_sq - num_sq
print "Time Taken:", time.time()-start


#input at 1 = actual squares
#input at 2 = squares * 2
#input at 3 = squares * 3.... hmmmm...

"""
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
"""
~/Desktop/python_projects/proj_euler $python prob193.py
0.607927102847
6.84465068462e+14
Time Taken: 20.8167331219

"""
