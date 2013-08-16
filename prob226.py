import time
START = time.time()
from math import log,sin,cos, pi, asin

sumz = 0
cx = .25
cy = .5
radius = .25
total_area = .25

def compute(x):
	total = 0
	for i in xrange(0,100):
		temp = (2**i * x) % 1
		temp = min(temp, (-1*temp)%1)
		total += temp / 2.**i
	return total

val = .1
for digit in xrange(2,15):
	min_dist = 5
	min_val = -20
	for i in xrange(-9,10):
		x_val = i/10.**digit + val
		y_val = compute(x_val)
		dist = .25 - ( (cx - x_val)**2 + (cy - y_val)**2)**.5
		if abs(dist) < abs(min_dist):
			min_dist = dist
			min_val = x_val
	val = min_val
	print val

area_start = val # 0.0789077879653  # would be computed value
area_end = .5
angle = (asin((.25-area_start)/.25) /pi * 180)

circle_area = radius ** 2 * pi * angle/360.  # the slice portion of the circle
circle_area += (.25 - area_start) * (.5 - compute(area_start))/2
rectangle_area = .5 *(area_end-area_start)
print rectangle_area, "This is the area we want to remove via a rectangle"
print circle_area, "This is the area of the circle that we want to add back on."

early_area = 0

print "The total area is:", total_area - early_area - rectangle_area + circle_area


print "Time Taken:", time.time() - START
