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
	for i in xrange(0,200):  # THIS IS AN APPROXIMATION
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
angle = (asin((.25-area_start)/.25) /pi * 180)  + 90


print "start:", round(area_start,4), "end:", area_end
print "angle is:", angle
circle_area = radius ** 2 * pi * angle/360.  # the slice portion of the circle
circle_area += (.25 - area_start) * (.5 - compute(area_start))/2
rectangle_area = .5 *(area_end-area_start)
print rectangle_area, "This is the area we want to remove via a rectangle"
print circle_area, "This is the area of the circle that we want to add back on."

early_area = 0
ratio = 10**7. # THIS IS AN APPROXIMATION
for i in xrange(0, int(area_start * ratio)):
	early_area += compute(i/ratio) / ratio
	if i % 1024 == 0:
		print i

print "The total area is:", round(total_area - early_area - rectangle_area + circle_area, 8)


print "Time Taken:", time.time() - START


"""
Congratulations, the answer you gave to problem 226 is correct.

You are the 1045th person to have solved this problem

The total area is: 0.11316017
Time Taken: 263.636204004

I suggest that if you're interested in this problem, you look at my code in helper226.py :). It creates a nice visualization of what the blancmange looks like. Quite a bit of regret on my part for not doing this cool problem earlier.
"""

