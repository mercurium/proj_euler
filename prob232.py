import time
START = time.time()

import operator as op
def ncr(n, r):
    r = min(r, n-r)
    if r == 0: return 1
    if r <  0: return 0
    num = reduce(op.mul, xrange(n, n-r, -1))
    denom = reduce(op.mul, xrange(1, r+1))
    return num//denom

p1 = .5
p2 = [1- .5**6, 1-.5**5, 1-.5**2]

player1 = [0,0]
player2 = [0] * 501

for i in xrange(2,10000):
    player1.append( ncr(i-1,99) * p1**i) # This is correct
print "Time Taken:", time.time() - START

mult = 1-p2[0]
for i in xrange(1,len(player2)):
    mult2 = mult * (1-p2[1])
    for j in xrange(i+1,len(player2)):
        mult *= p2[0]
        for k in xrange(j+1,len(player2)):
            player2[k] += mult2 * p2[2]**(k-j-1) * (1-p2[2])
        mult2 *= p2[1]
    mult *= p2[0]

win_ratio = 0
for i in xrange(len(player2)):
    win_ratio += player2[i] * sum(player1[i+1:])

print win_ratio
print sum(player1), sum(player2)

print [round(x,5) for x in player2[:10]]

print "Time Taken:", time.time() - START


"""
Player 2 should bet 64 points, then 32, then 4. 


"""
