import time
START = time.time()
SIZE  = 4

costs = [[0,0,0,0],[0,0,1,1],[0,1,1,3],[0,1,3,3]]
squares = set([1,4,9,16,25])

count = 0
for a in xrange(0,SIZE):
  for b in xrange(0,SIZE):
    for c in xrange(0,SIZE):
      for d in xrange(0,SIZE):
        total_cost = costs[a][b] + costs[b][c] + costs[c][d] + costs[d][a] + a+b+c+d +1
        if total_cost in squares:
          print a+1,b+1,c+1,d+1, total_cost
          count += 1

print count
print "Time taken:", time.time() - START

'''
Triangles (0,0), (a,0), (0,b)
point (a,b) is in the triangle


'''
