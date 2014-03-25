import string, time
from heapq import *

START = time.time()


fileRead = open('matrix.txt','r')
matrix = string.split(fileRead.read(),'\n') #Reading in the matrix and splitting it into rows

matrix = [string.split(row,",") for row in matrix] #Splitting the matrix rows into individual entries
matrix = matrix[:-1] +matrix[-1][:-1] #Clean off junk at the ends

matrix = [ [int(x) for x in row ] for row in matrix] #int-ifying the matrix

SIZE = len(matrix)

# -1 to symbolize that the element has not been traversed before.
answer = [ [-1]*SIZE for i in range(SIZE) ] #making the original solution matrix.

heap =[]
heapify(heap)
for i in xrange(0,SIZE):
    heappush(heap, (matrix[i][0],i,0))


while len(heap) > 0:
    nextVal = heappop(heap)
    currentCost, x,y= nextVal

    if x < SIZE-1 and answer[x+1][y] == -1:
        heappush(heap, (matrix[x+1][y] +currentCost,x+1,y))
    if y < SIZE-1 and answer[x][y+1] == -1:
        heappush(heap, (matrix[x][y+1] +currentCost,x,y+1))
    if x > 0 and answer[x-1][y] == -1:
        heappush(heap, (matrix[x-1][y] +currentCost,x-1,y))

    if answer[x][y] == -1 or answer[x][y] > currentCost:
        answer[x][y] = currentCost


print min([col[-1] for col in answer]) 
print "Time Taken:", time.time() - START


"""
Basic idea behind this algorithm is to run Dijkstra's with a priority queue, and enter in new values based on which one costs the least to add at the moment. 
Runtime is:
time taken: 0.123919963837, which got better after I changed my previous foolishness of using string -> int -> string conversino. hehe. It's nice to improve xD;;
answer was 260324


"""
