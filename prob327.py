import time, math
START = time.time() 

def numCards(numRooms, limit):
    if numRooms +1 <= limit:
        return numRooms +1
    if limit < 3:
        return -1
    oneLessRoom = numCards(numRooms -1, limit)
    numHaulTrips = int(math.ceil((oneLessRoom - limit +1) / (limit - 2.)))
    return numHaulTrips * 2 + oneLessRoom +1

print sum( [numCards(30, cards) for cards in range(3,41)])
print "Time Taken:", time.time() - START


"""
So, my key insight was this. Why not work backwards from the goal to the start point? If I need x keys at the beginning of N rooms, then I need Y keys to get x keys from room N+1. Since I can move (Lim-2) cards per trip, moving the cards over will take me X/(lim-2) trips, which incurs an extra 2X/(lim-2) steps. Beyond that, everything else recurses nicely so I'm amazed that I didn't manage to solve this earlier...


17:21 ~/Desktop/python_projects/proj_euler $ python prob327.py 
34315549139516
Time Taken: 0.000369071960449


Congratulations, the answer you gave to problem 327 is correct.

You are the 653rd person to have solved this problem.

Nice work, mercurium, you've just advanced to Level 10.
685 members (0.17%) have made it this far.

You have earned 1 new award:

Lucky Luke: Solve fifty lucky numbered problems

"""
