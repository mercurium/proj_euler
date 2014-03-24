import time
start = time.time()

SIZE = 2

# sides = number of sides that this subproblem contains
# edge1 = number of points that the left side edge has left
# edge2 = number of points that the right side edge has left.
# side_len = length of the side when the whole side is there
def count(sides, edge1, edge2, side_len):
    if sides == 1:
        return 1
    sumz = 0
    if sides == 2:
        for i in xrange(1,edge1):
            sumz += count(1,i,i,side_len) * count(2,edge1-i,edge2,side_len)
        sumz += 
    

print "Time Taken:", time.time() - start


# hurr... of course it's not as easy as I thought it would be... :[
