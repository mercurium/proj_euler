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
answer[0][0] = matrix[0][0]


heap =[]
heapify(heap)
heappush(heap, (matrix[0][1]+matrix[0][0],0,1))
heappush(heap, (matrix[1][0]+matrix[0][0],1,0))

while len(heap) > 0:
    nextVal = heappop(heap)
    currentCost, x,y= nextVal
    if x < SIZE-1 and answer[x+1][y] == -1: #RIGHT
        heappush(heap, (matrix[x+1][y] +currentCost,x+1,y))
    if x > 0 and answer[x-1][y] == -1: #LEFT
        heappush(heap, (matrix[x-1][y] +currentCost,x-1,y))
    if y < SIZE-1 and answer[x][y+1] == -1: #DOWN
        heappush(heap, (matrix[x][y+1] +currentCost,x,y+1))
    if y > 0 and answer[x][y-1] == -1: #UP
        heappush(heap, (matrix[x][y-1] +currentCost,x,y-1))


    if answer[x][y] == -1 or answer[x][y] > currentCost:
        answer[x][y] = currentCost



print answer[-1][-1]
print "Time taken:", time.time() - START

"""
Haha, this one is another implementation of dijkstra's algorithm. It follows pretty easily from problem 82 so there's nothing new here.

"""
