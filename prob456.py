import time
start = time.time()

SIZE =  2*10**6
def bsearch(lst,num, start=0,end=-1):
    if end == -1:
        end = len(lst)
    index = (start+end)/2

    if start == end-1:
        return index+1,len(lst)-index-1
    if lst[index] > num:
        return bsearch(lst,num,start,(start+end)/2)
    elif lst[index] < num:
        return bsearch(lst,num,(start+end)/2, end)

    start, end = index,index #looks slow/stupid, but realistically, there won't be that many points with same slope
    while lst[start] == num:
        start -=1
    while end < len(lst) and lst[end] == num:
        end +=1
    return start+1,len(lst)-end


def div(point):
    if point[1] == 0:
        return float('inf')
    return 1.0 * point[0]/point[1]


points = []
for i in xrange(1,SIZE+1):
    points.append( (pow(1248,i,32323)-16161, pow(8421,i,30103)-15051))

lst1 = [] #points above the x axis
lst2 = [] #points below the x axis
for point in points:
    if point[1] > 0:
        lst1.append(point) 
    elif point[1] < 0:
        lst2.append(point)
    elif point[0] > 0:
        lst1.append(point)
    else:
        lst2.append(point)

lst1Slopes = sorted([div(p) for p in lst1]) #sorted lists of the slopes from the points
lst2Slopes = sorted([div(p) for p in lst2])

### Bottleneck starts here, no need to worry about slower code above yet.... ###

count = 0
for i in xrange(len(lst1)):
    point = lst1[i]
    above,below = bsearch(lst2Slopes,div(point))
    count += above * below    
    if i%16384 == 0: #counter variable to see how it's doing
        print i


for i in xrange(len(lst2)):
    point = lst2[i]
    above,below = bsearch(lst1Slopes,div(point))
    count += above * below    
    if i%16384 == 0: #counter variable to see how it's doing
        print i

print count
print "Time Taken:", time.time() - start

"""

RAAAH, this is O(n^2), not good LOL
Okay, so this is an extension of problem 184. If I had done the algorithm upgrade from O(n^2) to O(n log(n)) back then, I would have gotten first lol. Anyways, the pdf I have for problem 184 still holds, but if we sort the points based on their slope, then we can figure out which part of the line they're on for all points. After we get their slopes, we can run a binary search to see how many of them are less than the requested slope value.


Congratulations, the answer you gave to problem 456 is correct.

You are the 4th person to have solved this problem.

Time Taken: 27.6909570694
Answer is: 333333208685971546

"""
