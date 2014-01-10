import time
START = time.time()

old_prob = [0] * 50 + [1.] + [0,0,0]
prob = [0] * 54

avg_round = 0
for iteration in xrange(1,100000):
    for i in xrange(1,51):
        prob[i] +=  old_prob[i]/2.
        prob[i-2] += old_prob[i]/36.
        prob[i-1] += old_prob[i] * 2 / 9.
        prob[i+1] += old_prob[i] * 2 / 9.
        prob[i+2] += old_prob[i]/36.

    #Edge Cases
    prob[48] += prob[52]
    prob[49] += prob[51]
    prob[1] += prob[53]

    avg_round += iteration * (prob[0])
    old_prob = prob
    prob = [0] * 54

print "The answer is:", round(avg_round,10)

print "Time Taken:", time.time() - START


"""
This problem is actually not that complex. If we consider that there are only 51 different states (how far the coins are from each other), and that they interact with the 4 other states closest to them, we can just run a bunch of iterations until the entire thing converges. Yup yup, xD...

Congratulations, the answer you gave to problem 227 is correct.

You are the 1193rd person to have solved this problem.

You have earned 1 new award:

Prime Obsession: Solve fifty prime numbered problems

00:29 ~/Desktop/python_projects/proj_euler $ python prob227.py 
The answer is: 3780.618622
Time Taken: 6.25084590912


"""
