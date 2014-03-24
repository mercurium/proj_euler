import time, math
START = time.time()

point = (0,0,10.1)
next_pt = (1.4,-9.6)
count = 2

while True:
    la = math.atan2((next_pt[1] - point[1]),(next_pt[0] - point[0]))  #the line's angle
    sa = math.atan2(-.25*next_pt[1],next_pt[0]) # the slope's angle. -4x/y
    
    new_angle = math.pi + 2*sa - la #Angle of reflection off of the tangent line
    
    slope = math.tan(new_angle)
    const = next_pt[1] - next_pt[0] * slope
    
    a,b,c = slope*slope + 4, (2*slope*const), const*const - 100
    sol1, sol2 = (-b + math.sqrt(b**2 - 4 *a*c))/(2*a),  (-b - math.sqrt(b**2 - 4 *a*c))/(2*a)

    point = next_pt #We've finished calculations with the previous point, toss out old result
    
    if (sol1-next_pt[0])**2 < (sol2-next_pt[0])**2: #one of these is going to be the current pt
        next_pt = (sol2, sol2*slope + const)
    else: #grab the one that's not the point we're currently at.
        next_pt = (sol1, sol1*slope + const)
    count += 1

    if math.fabs(next_pt[0]) < .01 and next_pt[1] > 0:
        print count, point, next_pt
        break
    
print "Time Taken:", time.time() - START


"""
~/proj_euler $python prob144.py 
354 (-2.1156727696594517, 9.06066856953095) (0.005018072804256874, 9.999994963787799)
Time Taken: 0.00188589096069

2989th to solve it... xD

"""
