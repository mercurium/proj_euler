import string
import time
from heapq import *


temp = open('matrix.txt','r')
lst = string.split(temp.read(),'\n')
size = len(lst)-1
start = time.time()

for i in xrange(0,len(lst)):
  lst[i] = string.split(lst[i],',')

lst = lst[:-1] +lst[-1][:-1]
for i in xrange(0,len(lst)):
  for j in xrange(0, len(lst[i])):
    lst[i][j] = int(lst[i][j]) #this is just cleaning stuff

answer = []
for i in xrange(0,size):
  answer =answer+[[-1]*size]

answer[0][0] = lst[0][0]


heap =[]
heapify(heap)
heappush(heap, (lst[0][1]+lst[0][0],'0','1'))
heappush(heap, (lst[1][0]+lst[0][0],'1','0'))

while len(heap) > 0:
  item = heappop(heap)
  x,y= int(item[1]),int(item[2])
  if x < size-1 and answer[x+1][y] == -1:
    heappush(heap, (lst[x+1][y] +item[0],str(x+1),str(y)))
  if x > 0 and answer[x-1][y] == -1:
    heappush(heap, (lst[x-1][y] +item[0],str(x-1),str(y)))
  if y < size-1 and answer[x][y+1] == -1:
    heappush(heap, (lst[x][y+1] +item[0],str(x),str(y+1)))
  if y > 0 and answer[x][y-1] == -1:
    heappush(heap, (lst[x][y-1] +item[0],str(x),str(y-1)))
  if answer[x][y] == -1 or answer[x][y] > item[0]:
    answer[x][y] = item[0]



print answer[-1][-1]
print "time taken: " + str(time.time()-start)


