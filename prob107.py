from heapq import *
import string, time

START  = time.time()
file   = open('network.txt', 'r')
matrix = file.read().strip().replace('-', '0').split('\n')

for (index,row) in enumerate(matrix):
  matrix[index] = [int(col) for col in row.split(',')]

sumOfAllEdges = sum([ sum(row) for row in matrix]) / 2

branches = [0]
heap     = []
for i in xrange(0, len(matrix[0])):
  if matrix[0][i] != 0:
    heappush(heap, (matrix[0][i], 0, i))

sumz  = 0
count = 0
while len(branches) != 40:
  [val, start, end] = heappop(heap)
  if end not in branches:
    for i in xrange(0, len(matrix[0])):
      if matrix[end][i] != 0:
        heappush(heap, (matrix[end][i],end,i))
    branches += [end]
    sumz     += val
    count    += 1

print "Answer is :", sumOfAllEdges - sumz
print "Time Taken:", time.time() - START

