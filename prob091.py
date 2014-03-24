import string
import math
import time
start = time.time()

size = 3
true = 1
false = 0


def dist(p1,p2):
  return math.sqrt( (p1.x-p2.x)**2 + (p1.y-p2.y)**2)

def dist2(p1,p2):
  return (p1.x-p2.x)**2 + (p1.y-p2.y)**2

class Point:
  def __init__(self, x=0, y=0):
        self.x, self.y = int(x), int(y)
  
  def __print__():
        print self.x, self.y
        
ori = Point(0,0)

def pythag(p1,p2):
  d1,d2,d3 = dist2(p1,ori), dist2(p2,ori), dist2(p1,p2)
  if d1 == 0 or d2 == 0 or d3 == 0:
    return false
  if d1 + d2 == d3 or d1+d3 == d2 or d2+d3 == d1:
    return true
  return false

def fn(size):
  count = 0
  for x1 in range(0,size+1):
    for x2 in range(0,x1+1):
      for y2 in range(0,size+1):
        for y1 in range(0,y2+1):
          p1 = Point(x1,y1)
          p2 = Point(x2,y2)
          if (p1.x != 0 or p1.y != 0) and (p2.x != 0 or p2.y != 0):
            if pythag(p1,p2):
              count = count + 1
            #print  str((p1.x,p1.y)) + ',' + str((p2.x,p2.y))
  print count, count - 3 * size **2, size

#for i in range(1,51):
fn(50)

print "Time taken: " + str(time.time() - start)

