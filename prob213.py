#NOTE TODO need to solve it
import string
import copy

size = 32
ta = [[]]*size
ta2 =[[]]*size

for i in xrange(0,len(ta)):
    ta[i] = [1.0]*size
    ta2[i] = [0]*size
zeroes = copy.deepcopy(ta2)

for numloops in xrange(0,50):
    ta2 = copy.deepcopy(zeroes)
    for i in xrange(1, size-1):
        for j in xrange(1,size-1):
            chance = 4
            if i == 1 or i == size-2:
                chance -= 1
            if j == 1 or j == size-2:
                chance -= 1
            ta2[i-1][j] += ta[i][j]/chance
            ta2[i+1][j] += ta[i][j]/chance
            ta2[i][j-1] += ta[i][j]/chance
            ta2[i][j+1] += ta[i][j]/chance
    ta = copy.deepcopy(ta2)
#for i in xrange(0,size):
#    for j in xrange(0,size):
#        ta2[i][j] = round(ta2[i][j],4)
        
#for i in xrange(0,size):
#    print ta2[i]
    
sumz = 0
for i in xrange(1, size-1):
    for j in xrange(1,size-1):
            sumz +=1 -ta2[i][j]
print sumz









