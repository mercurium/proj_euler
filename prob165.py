#NOTE TODO need to solve it
import time
from fractions import Fraction

START = time.time()
SIZE  = 5000

class Point():
  def __init__(self, x,y):
    self.x = x
    self.y = y

  def toString(self):
    return "(" + str(self.x) +"," + str(self.y)+ ")"

class Line():
  def __init__(self, start,end):
    if start.x > end.x:
      start,end = end,start

    self.start = start
    self.end   = end

    if start.x != end.x:
      self.slope = Fraction((end.y - start.y),(end.x - start.x))
    else:
      self.slope = 10**6
    self.yInter = start.y - self.slope * start.x

  def isIntersecting(self, l):
    if self.slope == l.slope:
      return False

    if self.end.x < l.start.x \
        or self.start.x > l.end.x \
        or max(self.end.y,self.start.y) < min(l.start.y,l.end.y) \
        or min(self.end.y,self.start.y) > max(l.start.y,l.end.y):
          return False

    if self.slope == 10**6:
      intersect = l.yInter + self.start.x * l.slope
      if intersect < max(self.start.y, self.end.y) and intersect > min(self.start.y, self.end.y):
        intersectionPoints.add((self.start.x, intersect))
        return True
      return False

    if l.slope == 10**6:
      intersect = self.yInter + l.start.x * self.slope
      if intersect < max(l.start.y, l.end.y) and intersect > min(l.start.y, l.end.y):
        intersectionPoints.add((l.start.x, intersect))
        return True
      return False

    if self.slope == 0:
      intersect = (self.start.y - l.yInter) / l.slope
      if intersect > self.start.x and intersect < self.end.x:
        intersectionPoints.add((intersect, self.start.y))
        return True
      return False

    if l.slope == 0:
      intersect = (l.start.y - self.yInter) / self.slope
      if intersect > l.start.x and intersect < l.end.x:
        intersectionPoints.add((intersect, l.start.y))
        return True
      return False


    intersect  = (self.yInter - l.yInter) / (l.slope - self.slope)
    intersectY = self.yInter + intersect * self.slope

    if intersect < self.end.x and \
        intersect > self.start.x and \
        intersect < l.end.x and \
        intersect > l.start.x:
      intersectionPoints.add((intersect, intersectY))
      return True
    return False

  def toString(self):
    return "Line(" +self.start.toString() + "," + self.end.toString() + ")"


n     = 290797
mod   = 50515093
lines = []
for i in range(SIZE):
  vals = [pow(n,2,mod) % 500, pow(n,4,mod) % 500, pow(n,8,mod) % 500, pow(n,16,mod) % 500]
  n    = pow(n,16,mod)
  lines.append(Line(Point(vals[0], vals[1]), Point(vals[2], vals[3])))

print lines[0].toString()
count  = 0
intersectionPoints = set()
for i in range(SIZE):
  for j in range(i+1,SIZE):
    if lines[i].isIntersecting(lines[j]):
      count +=1
  if i% 100 == 0:
    print i, count
print len(intersectionPoints)

print count
print "Time Taken:", time.time() - START
