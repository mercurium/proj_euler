from heapq import *
import string
import time
start_time = time.time()

file = open('network.txt', 'r')
matrix = string.split(file.read(),'\n')

if len(matrix) == 41:
  matrix = matrix[:-1]
for i in range(0,len(matrix)):
  matrix[i] = string.split(matrix[i],',')
  for j in range(0,len(matrix)):
    if matrix[i][j] != '-':
      matrix[i][j] = int(matrix[i][j]) #up to here is just cleaning the list
      
      
print "Time Taken: " + str(time.time()-start_time)



silly_sum = 0
for i in range(0,len(matrix)):
  for j in range(0,i):
    if matrix[i][j] != '-':
      silly_sum += matrix[i][j]
#this is the adding of the total weight from before


vars = [0]
heap = []
for i in range(0, len(matrix[0])):
  if matrix[0][i] != '-':
    heappush(heap, (matrix[0][i],'0', str(i)))
#each priority queue entry has: (bridge val, start, end)

sumz = 0
count = 0
while len(vars) != 40:
  item = heappop(heap)
  val = item[0]
  start = int(item[1])
  end = int(item[2])
  if end not in vars:
    for i in range(0, len(matrix[0])):
      if matrix[end][i] != '-':
        heappush(heap, (matrix[end][i],item[2],str(i)))
    vars += [end]
    sumz+= val
    count+=1

print len(vars), count

print silly_sum -sumz, silly_sum, sumz

print "Time Taken: " + str(time.time()-start_time)








