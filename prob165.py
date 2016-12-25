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

    def __eq__(self, point):
        return self.x == point.x and self.y == point.y

    def __ne__(self, point):
        return not self.__eq__(point)

    def toString(self):
        return "(" + str(self.x) +"," + str(self.y)+ ")"

    def toTuple(self):
        return (self.x, self.y)

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

    def __eq__(self, line):
        return self.start == line.start and self.end == line.end

    def __ne__(self, line):
        return self.__eq__(line)

    def inBounds(self, point):
        if self.start.x > point.x \
          or self.end.x < point.x \
          or min(self.start.y, self.end.y) > point.y \
          or max(self.start.y, self.end.y) < point.y:
            return False
        if (point.x == self.start.x or point.x == self.end.x) \
          and self.start.x != self.end.x:
            return False
        if (point.y == self.start.y or point.y == self.end.y) \
           and self.start.y != self.end.y:
            return False
        return True

    def isIntersecting(self, l):
        if self.slope == l.slope:
            return False

        if self.start.x >= l.end.x \
          or self.end.x <= l.start.x \
          or min(self.start.y, self.end.y) >= max(l.start.y, l.end.y) \
          or max(self.start.y, self.end.y) <= min(l.start.y, l.end.y):
            return False

        if self.slope == INF_SLOPE:
            return compareInfSlopeTONormalLine(self, l)

        if l.slope == INF_SLOPE:
            return compareInfSlopeTONormalLine(l, self)

        if self.slope == 0:
            return compareZeroSlopeLineToNormalLine(self, l)

        if l.slope == 0:
            return compareZeroSlopeLineToNormalLine(l, self)

        intersectX = -1 * (self.yInter - l.yInter) / (self.slope - l.slope)
        intersectY = intersectX * self.slope + self.yInter
        
        intersect  = Point(intersectX, intersectY)
        
        if self.inBounds(intersect) and l.inBounds(intersect):
            intersectionPoints.add(intersect.toTuple())
            return True
        return False

    def toString(self):
        return "Line(" +self.start.toString() + "," + self.end.toString() + ")"


def compareInfSlopeTONormalLine(infLine, normalLine):
    intersect = normalLine.yInter + infLine.start.x * normalLine.slope
    p         = Point(infLine.start.x, intersect)

    if infLine.inBounds(p) and normalLine.inBounds(p):
        intersectionPoints.add(p.toTuple())
        return True
    return False

def compareZeroSlopeLineToNormalLine(zeroSlopeLine, normalLine):
    intersect = normalLine.xInter + zeroSlopeLine.start.y / normalLine.slope
    p         = Point(intersect, zeroSlopeLine.start.y)

    if zeroSlopeLine.inBounds(p) and normalLine.inBounds(p):
        intersectionPoints.add(p.toTuple())
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
count = 0 # count non-distinct intersection points

intersectionPoints = set()
for i in xrange(SIZE):
    for j in xrange(i+1,SIZE):
        if lines[i].isIntersecting(lines[j]):
            count +=1
    if i% 100 == 0:
        print i, count, len(intersectionPoints)

print "Answer:", len(intersectionPoints)
print "Time Taken:", time.time() - START


"""
Congratulations, the answer you gave to problem 165 is correct.

You are the 1802nd person to have solved this problem.

Answer: 2868868
Time Taken: 107.298945189

Holy shit, this was such a huge pain in the ass to solve -_-;;

Sooooo many edge cases and places to introduce bugs -__-; Actual algorithm is really simple, take all 5000 lines, compare them pairwise, see if they intersect. Just gotta handle all the edge cases...

"""
