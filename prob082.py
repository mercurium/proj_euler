import string
import time
from heapq import *

start = time.time()


temp = open('matrix.txt','r')
lst = string.split(temp.read(),'\n')
for i in xrange(0,len(lst)):
  lst[i] = string.split(lst[i],',')

lst = lst[:-1] +lst[-1][:-1]
for i in xrange(0,len(lst)):
  for j in xrange(0, len(lst[i])):
    lst[i][j] = int(lst[i][j]) #this is just int-ifying stuff

size = len(lst)

answer = []
for i in xrange(0,size):
  answer = answer+[[-1]*size]

heap =[]
heapify(heap)
for i in xrange(0,size):
  heappush(heap, (lst[i][0],str(i),'0'))


while len(heap) > 0:
  item = heappop(heap)
  x,y= int(item[1]),int(item[2])
  if x < size-1 and answer[x+1][y] == -1:
    heappush(heap, (lst[x+1][y] +item[0],str(x+1),str(y)))
  if y < size-1 and answer[x][y+1] == -1:
    heappush(heap, (lst[x][y+1] +item[0],str(x),str(y+1)))
  if x > 0 and answer[x-1][y] == -1:
    heappush(heap, (lst[x-1][y] +item[0],str(x-1),str(y)))
  if answer[x][y] == -1 or answer[x][y] > item[0]:
    answer[x][y] = item[0]


ans_lst = [0]*size #getting the last column
for i in range(0,size):
  ans_lst[i] = answer[i][-1]
print min(ans_lst)
print "time taken: " + str(time.time()-start)


