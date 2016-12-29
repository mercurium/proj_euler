import time, math
START = time.time()
SIZE = 100

def velocity(p1, p2):
    if p1[1] == p2[1]:
        return p1[1]
    else:
        return (p2[1] - p1[1]) / ( math.log(p2[1]) - math.log(p1[1]))

def distance(p1, p2):
    return math.sqrt((p1[0]-p2[0])**2+ (p1[1] - p2[1])**2)

def cost_route(p1, p2):
    return distance(p1,p2) / velocity(p1,p2)

def updateMinVal(valDict, key, val, entry):
    if key not in valDict:
        valDict[key] = (val, entry)
    elif valDict[key][0] > val:
        valDict[key] = (val, entry)

costs = { (0,1) : (0, None) } 
for x in xrange(1,SIZE+1):
    print x
    for entry in costs.keys():
        for y in xrange(1, SIZE):
            cost = costs[entry][0] + cost_route((x,y), entry)
            updateMinVal(costs, (x,y), cost, entry)
    
for entry in costs.keys():
    x = SIZE
    y = 1
    cost = costs[entry][0] + cost_route((x,y), entry)
    updateMinVal(costs, (x,y), cost, entry)

cost, prev = costs[(SIZE,1)]
while prev != None:
    print cost, prev
    cost, prev = costs[prev]

print "Time Taken:", time.time() - START


"""
1666 4640 2 499 18.8528104209
1666 4982 2 2537 18.5827906416
2276 5036 130 2738 18.5696552345
2200 3998 5363 86 1217 2904 18.5235163522
[1, 656, 1833, 3087, 4388, 4889] [0, 14, 352, 1070, 2535, 4034] 18.4512660003
is a hard limit on how big it can be.

[1, 11, 17, 26, 35, 46, 53] [0, 1, 3, 6, 13, 29, 47] 9.24596933422
[1, 11, 19, 23, 39, 45, 49] [0, 1, 4, 6, 19, 28, 43] 9.23781289606
[1, 12, 18, 23, 33, 40, 45, 49] [0, 1, 3, 5, 11, 18, 29, 46] 9.23538839065


[1, 3, 4, 5] [0, 1, 1, 2] 4 4.66818783436
"""
