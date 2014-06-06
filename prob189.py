#NOTE TODO need to solve it
import time
START = time.time()
height = 1

triangle = [ [-1] * (2*x+1) for x in range(0,height)]

for i in xrange(0, 3**(height**2)):
    for h in range(height):
        for col in range(len(triangle[h])):
            triangle[h][col] = i/(3**(h+col)) % 3
            if triangle[h][col] == 

print "Time Taken:", time.time() - START

"""


"""
