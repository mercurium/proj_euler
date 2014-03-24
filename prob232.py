import time
START = time.time()


#key format = (p1points,p2points,whosTurn)
#value = chance of winning from there.
optimal = dict()
for i in range(101): #We want p2 to win. Base cases
    optimal[(i,100,0)] = 1.0
    optimal[(i,100,1)] = 1.0
    optimal[(100,i,0)] = 0
    optimal[(100,i,1)] = 0

def getOptimal(p1,p2, turn): 
    p1, p2 = min(100,p1), min(100,p2) #if we go over 100, assume we win at 100 pts
    if (p1,p2,turn) in optimal: #if we computed it before, reuse result
        return optimal[(p1,p2,turn)]
    elif turn == 0: #if player 0 is going, flip ordinary coin
        optimal[(p1,p2,turn)] = getOptimal(p1+1,p2,1)/2. + getOptimal(p1,p2,1)/2.
    else: #otherwise player 1 is going, flip n times 
        bestVal = 0.0
        for i in range(1,9): #figure out which condition is optimal at each state.
            val = (2**(i+1)/(2**i+1.))*(getOptimal(p1,p2+2**(i-1),0)/(2**i) + ((2**i-1.)/(2**(i+1) )* getOptimal(p1+1,p2,1)))
            if val > bestVal:
                bestVal = val
        optimal[(p1,p2,turn)] = bestVal
    return optimal[(p1,p2,turn)]

for i in range(99,-1,-1): #to make sure we don't break the recursion limit
    for j in range(99,-1,-1):
        getOptimal(i,j,0)


print getOptimal(0,0,0)
print "Time Taken:", time.time() - START



"""
Congratulations, the answer you gave to problem 232 is correct.

You are the 1047th person to have solved this problem.
~/proj_euler $python prob232.py 
0.836485555847
Time Taken: 0.235028982162

This is a simple dynamic programming problem, where we can determine what the expected chance of winning is from each state and get results from previous states. Really standard DP.


"""
