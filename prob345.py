import time
import string
from itertools import combinations as comb

START = time.time()
SIZE  = 15

input_file = open('data345.txt','r')
input_data = input_file.read()

#converting characters to numbers
def v(charz):
  return ord(charz) - 97

#this is the initial setup of the matrix
matrix = string.split(input_data,'\n')
for i in xrange(0,len(matrix)):
  matrix[i] = [int(x) for x in filter(len, string.split(matrix[i],' ')) ]

vals = dict()

for i in xrange(0,SIZE):
  vals[(i,)] = matrix[SIZE-1][i]

#iterate through all possibilities, at each level pick the best possibility from the given results. I think this was O(2^n)?
for num in xrange(2,SIZE+1):
  for tup in comb('abcdefghijklmno',num):
    tup      = tuple([v(c) for c in tup])
    maxValue = 0
    for slot in range(len(tup)):
      val      = matrix[15-num][tup[slot]] \
               + vals[tup[:slot]           \
               + tup[slot+1:]]
      maxValue = val if maxValue < val else maxValue
    vals[tup] = maxValue

print vals[tuple(range(0,15))]
print "Time Taken:", time.time()- START

#the basis my solution for this problem was dynamic programming(I think?). Not too sure...

"""
13938
Time Taken: 0.229345083237
"""
