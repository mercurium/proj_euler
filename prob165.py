#NOTE TODO need to solve it
import time
START = time.time()

def sign(n):
	if n >0:
		return 1
	if n == 0:
		return 0
	return -1

class Point():
	def __init__(self, x,y):
		self.x = x
		self.y = y

class Line():
	def __init__(self, start,end):
		if start.x > end.y:
			start,end = end,start
		self.start = start
		self.end = end
		if start.x != end.x:
			self.slope = (end.y - start.y)*1.0/(end.x - start.x)
		else:
			self.slope = 10**6
		self.yInter = start.y - self.slope * start.x

	def isIntersecting(self, l):
		if self.slope == l.slope:
			return False
		if self.slope == 10**6:
			if l.slope == 10**6:
				return False
			if l.start.x < self.x and l.end.x > self.start.x and 


		a = sign(l.end.y - self.slope * l.end.x - self.yInter)
		b = sign(l.start.y - self.slope * l.start.x - self.yInter)
		c = sign(self.end.y - l.slope * self.end.x - l.yInter)
		d = sign(self.start.y - l.slope * self.start.x - l.yInter)
		if a == 0 or b== 0 or c == 0 or d == 0:
			return False
		if a != b and c != d:
			return True
		return False

n = 290797
mod = 50515093
lines = []
for i in range(5000):
	n = n*n%mod
	xS = n % 500
	n = n*n%mod
	yS = n % 500
	n = n*n%mod
	xE = n % 500
	n = n*n%mod
	yE = n% 500
	lines.append(Line(Point(xS,yS),Point(xE,yE)))

count = 0
for i in range(5000):
	for j in range(i+1,5000):
		if lines[i].isIntersecting(lines[j]):
			count +=1
	if i% 100 == 0:
		print i, count

print count
print "Time Taken:", time.time() - START
