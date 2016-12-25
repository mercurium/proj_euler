#NOTE TODO need to solve it
import time
from fractions import Fraction

START      = time.time()
SIZE       = 5000
INF_SLOPE  = 10**5 # Arbitrary marker value > max possible slope here
MOD        = 50515093
START_SEED = 290797

class Point():
    def __init__(self, x,y):
        self.x = x
        self.y = y

    def eq(self, point):
        return self.x == point.x and self.y == point.y

    def toString(self):
        return "(" + str(self.x) +"," + str(self.y)+ ")"

class Line():
        
    def __init__(self, start, end):
        if start.x > end.x:
            start, end = end, start

        self.start = start
        self.end   = end

        if start.x == end.x:
            self.slope = INF_SLOPE
        else:
            self.slope = Fraction((end.y - start.y), (end.x - start.x))

        self.yInter = start.y - self.slope * start.x
        if self.slope != 0:
            self.xInter = -self.yInter / self.slope
        else:
            self.xInter = self.xInter = self.yInter

    def eq(self, line):
        return self.start.eq(line.start) and self.end.eq(line.end)

    def inBounds(self, point):
        if min(self.start.x, self.end.x) > point.x \
          or max(self.start.x, self.end.x) < point.x \
          or min(self.start.y, self.end.y) > point.y \
          or max(self.start.y, self.end.y) < point.y:
            return False
        if self.start.x != self.end.x and point.x == self.start.x:
            return False
        if self.start.y != self.end.y and point.y == self.start.y:
            return False
        return True

    def isIntersecting(self, l):
        if self.slope == l.slope:
            return False

        if self.end.x < l.start.x \
            or self.start.x > l.end.x \
            or max(self.end.y,self.start.y) < min(l.start.y,l.end.y) \
            or min(self.end.y,self.start.y) > max(l.start.y,l.end.y):
                return False

        if self.slope == INF_SLOPE:
            return compareInfSlopeTONormalLine(self, l)

        if l.slope == INF_SLOPE:
            return compareInfSlopeTONormalLine(l, self)

        if self.slope == 0:
            return compareZeroSlopeLineToNormalLine(self, l)

        if l.slope == 0:
            return compareZeroSlopeLineToNormalLine(l, self)

        intersectX = (self.yInter - l.yInter) / (l.slope - self.slope)
        intersectY = self.yInter + intersectX * self.slope
        
        intersect  = Point(intersectX, intersectY)
        
        if self.inBounds(intersect) and l.inBounds(intersect):
            intersectionPoints.add((intersectX, intersectY))
            return True
        return False

    def toString(self):
        return "Line(" +self.start.toString() + "," + self.end.toString() + ")"


def compareInfSlopeTONormalLine(infLine, normalLine):
    intersect = normalLine.yInter + infLine.start.x * normalLine.slope # TODO fix

    p = Point(infLine.start.x, intersect)

    if infLine.inBounds(p) and normalLine.inBounds(p):
        intersectionPoints.add((infLine.start.x, intersect))
        return True
    return False

def compareZeroSlopeLineToNormalLine(zeroSlopeLine, normalLine):
    intersect = normalLine.xInter + zeroSlopeLine.start.y / normalLine.slope  # TODO fix

    p = Point(intersect, zeroSlopeLine.start.y)

    if zeroSlopeLine.inBounds(p) and normalLine.inBounds(p):
        intersectionPoints.add((intersect, zeroSlopeLine.start.y))
        return True
    return False

def generatePoints(seed, numPoints):
    lines = []
    for i in range(numPoints):
        vals = [ pow(seed, 2, MOD) % 500, \
                 pow(seed, 4, MOD) % 500, \
                 pow(seed, 8, MOD) % 500, \
                 pow(seed,16, MOD) % 500]
        seed = pow(seed, 16, MOD)
        lines.append(Line(Point(vals[0], vals[1]), Point(vals[2], vals[3])))
    return lines


lines = generatePoints(START_SEED, SIZE)
count = 0
print lines[0].toString()

intersectionPoints = set()
for i in xrange(SIZE):
    for j in xrange(i+1,SIZE):
        if lines[i].isIntersecting(lines[j]):
            count +=1
    if i% 100 == 0:
        print i, count, len(intersectionPoints)

print len(intersectionPoints)


l1 = Line(Point(0,8), Point(8,0))
l2 = Line(Point(0,0), Point(15,25))

l1.isIntersecting(l2)



print count
print "Time Taken:", time.time() - START
