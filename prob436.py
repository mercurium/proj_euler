#NOTE TODO need to solve it
import time,random
START = time.time()


count = 0
SIZE = 100
#for iteration in xrange(SIZE):
#    s1,s2 = 0,0
#    n1 = random.random()
#    while s1 < 1:
#        s1 += n1
#        n1 = random.random()
#    n2 = random.random()
#    while s2 < 2:
#        s2 += n2
#        n2 = random.random()
#    if n1 < n2:
#        count +=1
#print "Out of", SIZE, "rounds, player 2 won:", count 


a = [ [0]*SIZE for x in range(SIZE*2)]
for arr in range(len(a)):
    for i in range(SIZE):
        if arr-i <= 0:
            a[arr][i] += 1./SIZE
        else:
            for j in range(SIZE):
                a[arr][j] += a[arr-1-i][j]/SIZE

print [round(x,4) for x in a[SIZE-1]], '\n\n'
print [round(x,4) for x in a[2*SIZE-1]], '\n'
print [round(sum(a[2*SIZE-1][:j+1])/a[2*SIZE-1][0],4) for j in range(len(a[2*SIZE-1])) ]

prob = 0
for player1 in range(SIZE):
    for player2 in range(player1+1,SIZE):
        prob += a[SIZE-1][player1] * a[2*SIZE-1][player2]

tie = 0
for i in range(SIZE):
    tie += a[SIZE-1][i] * a[2*SIZE-1][i]

print prob, tie, prob/(1-tie)

print "Time Taken:", time.time() - START
