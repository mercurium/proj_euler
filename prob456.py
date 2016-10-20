import time
START = time.time()
SIZE  = 2*10**6

def bsearch(lst,num):
  if lst[-1] < num or lst[0] > num:
    return 0,0

  start = 0
  end   = len(lst)
  index = (start+end)/2

  while True:
    if start == end-1:
      start = index + 1
      end   = len(lst) - start
      return start, end
    if lst[index] > num:
      end   = index
      index = (start+end)/2
    elif lst[index] < num:
      start = index
      index = (start+end)/2
    else:
      break

  #looks slow/stupid, but realistically, there won't be that many points with same slope
  start, end = index,index
  while lst[start] == num:
    start -= 1
  while end < len(lst) and lst[end] == num:
    end   += 1
  return start + 1, len(lst) - end

def div(point):
  if point[1] == 0:
    return float('inf')
  return 1.0 * point[0]/point[1]


points = [(1248,8421)]
for i in xrange(SIZE-1):
  x = points[-1][0] * 1248 % 32323
  y = points[-1][1] * 8421 % 30103
  points.append((x,y))

points = map( lambda (x,y): (x-16161,y-15051), points)

lst1   = [] #points above the x axis

lst1   = filter(lambda (x,y): y > 0 or (y == 0 and x > 0), points)
lst2   = filter(lambda (x,y): y < 0 or (y == 0 and x <= 0), points)

print "Time Taken:", time.time() - START

#sorted lists of the slopes from the points
lst1Slopes = sorted([div(p) for p in lst1])
lst2Slopes = sorted([div(p) for p in lst2])

print "Time Taken:", time.time() - START
### Bottleneck starts here, no need to worry about slower code above yet.... ###

count = 0
for point in lst1:
    above,below  = bsearch(lst2Slopes,div(point))
    count       += above * below

for point in lst2:
    above,below  = bsearch(lst1Slopes,div(point))
    count       += above * below

print count
print "Time Taken:", time.time() - START

"""

RAAAH, this is O(n^2), not good LOL
Okay, so this is an extension of problem 184. If I had done the algorithm upgrade from O(n^2) to O(n log(n)) back then, I would have gotten first lol. Anyways, the pdf I have for problem 184 still holds, but if we sort the points based on their slope, then we can figure out which part of the line they're on for all points. After we get their slopes, we can run a binary search to see how many of them are less than the requested slope value.


Congratulations, the answer you gave to problem 456 is correct.

You are the 4th person to have solved this problem.

Time Taken: 27.6909570694
Time Taken: 2.47751903534 # switched to pypy and used less computationally stupid methods xD

Answer is: 333333208685971546

"""
