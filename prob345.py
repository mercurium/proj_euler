import time
start = time.time()
import string
from itertools import combinations as comb

file = open('prob345lst.txt','r')
file = file.read()

#converting characters to numbers
def v(charz): return ord(charz) - 97

#this is the initial setup of the matrix
matrix = string.split(file,'\n')
for i in xrange(0,len(matrix)):
  matrix[i] = filter((lambda x: x != ''), string.split(matrix[i],' '))
  for j in xrange(0,len(matrix[i])):
    matrix[i][j] = int(matrix[i][j])

vals = dict()

for i in xrange(0,15):
  vals[(i,)] = matrix[14][i]

#iterate through all possibilities, at each level pick the best possibility from the given results. I think this was O(n^3)?
for num in xrange(2,16):
  for tup in comb('abcdefghijklmno',num):
    tup = tuple([v(c) for c in tup])
    maxz = 0
    for slot in range(len(tup)):
      val = matrix[15-num][tup[slot]] + vals[tup[:slot]+tup[slot+1:]]
      if val > maxz:
        maxz = val
    vals[tup] = maxz

print vals[tuple(range(0,15))]
print "Time Taken:", time.time()- start

#the basis my solution for this problem was dynamic programming(I think?). Not too sure...

"""
13938
Time Taken: 0.229345083237
"""
