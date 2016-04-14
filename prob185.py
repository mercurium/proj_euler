#NOTE TODO need to solve it
import time
START = time.time()
SIZE = 16
NUMDIG = 10

data = open('data185.txt','r')
data = data.read()

guesses = [[int(x) for x in g] for g in data.split()[::2]]
correct = [int(x) for x in data.split()[1::2] ]
count = [0]

def recurse(pos, vals, appendedVals):
    if pos != 0:
        for g in sameSet[(pos-1,appendedVals[-1])]:
            vals[g] -=1
            if vals[g] < 0:
                return -1
    if pos == SIZE and vals == [0]*(len(guesses)):
        print pos, appendedVals, vals, "ANSWER"
        return appendedVals
    elif pos == SIZE:
        return -1
    for i in range(NUMDIG):
        if (pos,i) in sameSet:
            ans = recurse(pos+1, vals[:], appendedVals + [i])
            if ans != -1:
                return ans
    if pos < 6:
        print pos, appendedVals, vals
    return -1



sameSet = dict()
for g in range(len(guesses)):
    for index in range(SIZE):
        if (index, guesses[g][index]) in sameSet:
            sameSet[(index,guesses[g][index])].add(g)
        else:
            sameSet[(index,guesses[g][index])] = set([g])
for i in range(SIZE):
    for j in range(NUMDIG):
        if (i,j) in sameSet:
            print i,j, sameSet[(i,j)]

entries = sameSet.keys()
for entry in entries:
    if len(sameSet[entry]) < 2:
        del sameSet[entry]

#print recurse(0,correct[:], [])
print "Time Taken:", time.time()-START
