import time
START = time.time()

R = 105

points = []
for x in xrange(-1 * R + 1, R):
	for y in xrange(-1*R+1,R): #this could be optimized,but not worth it... 
		if x**2+y**2 < R**2:
			points.append((x,y))
points.remove((0,0))

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
#Because the thing is symmetrical, we only need to do it for half of the points, not both sets... =D 

def bsearch(lst,num, start=0,end=-1):
    if end == -1:
        end = len(lst)
    index = (start+end)/2

    if lst[index] == num:
        start, end = index,index #looks slow/stupid, but realistically, there won't be that many points with same slope
        while lst[start] == num:
            start -=1
        while end < len(lst) and lst[end] == num:
            end +=1
        return start+1,len(lst)-end
    if start == end-1:
        return index+1,len(lst)-index-1
    if lst[index] > num:
        return bsearch(lst,num,start,(start+end)/2)
    elif lst[index] < num:
        return bsearch(lst,num,(start+end)/2, end)



def div(point):
    if point[1] == 0:
        return float('inf')
    return 1.0 * point[0]/point[1]


lst1Slopes = sorted([div(p) for p in lst1]) #sorted lists of the slopes from the points
lst2Slopes = sorted([div(p) for p in lst2])

### Bottleneck starts here, no need to worry about slower code above yet.... ###

count = 0
for i in xrange(len(lst1)):
    point = lst1[i]
    above,below = bsearch(lst2Slopes,div(point))
    count += above * below    


for i in xrange(len(lst2)):
    point = lst2[i]
    above,below = bsearch(lst1Slopes,div(point))
    count += above * below    

print count
print "Time Taken:", time.time() - START

"""
Congratulations, the answer you gave to problem 184 is correct.

You are the 796th person to have solved this problem.

Nice work, mercurium, you've just advanced to Level 8.
1144 members (0.35%) have made it this far.


1725323624056
Time Taken: 112.400161982

And upon changing the algorithm to O(n log(n)) it went to...
Time Taken: 0.270301818848
...wat

LOL SOOOO... the irony is that I've already solved this problem a long while back when I was applying for internships. Vivek from Hackerrank had me solve it as an interview question and I typed up the solution for it... sooo... the pretty solution is already there typed up... 
"""
