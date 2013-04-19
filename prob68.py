#6531031914842725 is the answer
#(6, 10, 9, 8, 7, 5, 3, 1, 4, 2)

from itertools import permutations as perm
import time

start = time.time()

enum_vals = perm(range(1,11))


sumz = [0]*5
works = 1
valid_set = set([])
for i in enum_vals:
  works = 1
  if 10 in i[5:] or 4 in i[:5] or 6 in i[1:]:
    continue
  sumz[0] = i[0]+i[5]+i[6]
  sumz[1] = i[1]+i[6]+i[7]
  sumz[2] = i[2]+i[7]+i[8]
  sumz[3] = i[3]+i[8]+i[9]
  sumz[4] = i[4]+i[9]+i[5]
  for j in xrange(0,4):
    if sumz[j] != sumz[j+1]:
      works = 0
      break
  if works:
    valid_set.add(i)
    
print len(valid_set)
for i in valid_set:
  print i
  


print "Time Taken: ", time.time() - start

#6531031914842725 is the answer

#~/Desktop/python_projects/proj_euler $python prob68.py
#(6, 10, 9, 8, 7, 5, 3, 1, 4, 2)
#Time Taken:  2.69140601158


