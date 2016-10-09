import time, string
START = time.time()
from itertools import combinations

data    = open('sets.txt', 'r')
data    = data.read()
subsets = string.split(data.strip(), '\n')
for i in xrange(len(subsets)):
  subsets[i] = [int(x) for x in string.split(subsets[i],',')]

sumz  = 0
for index in xrange(len(subsets)):
  setz        = subsets[index]
  subset_sums = set([0])
  SET_SIZE    = len(setz)
  works       = True
  for i in xrange(1,SET_SIZE):
    if not works:
      break
    prev_max    = max(subset_sums)
    subset_sums = set()
    for j in combinations(range(SET_SIZE),i):
      k = sum( setz[l] for l in j)
      if k in subset_sums or k <= prev_max:
        works = False
        break
      else:
        subset_sums.add(k)
  if works:
    sumz += sum(setz)
    print "This set works:", setz
    print sum(setz), index, sumz

print sumz
print "Time Taken:", time.time() - START

"""
Congratulations, the answer you gave to problem 105 is correct.

You are the 3559th person to have solved this problem.

Return to Problems page.

"""
