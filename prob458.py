import time
START = time.time()

count = [0] * 7
count[1] =7
SIZE = 25* 10**7
MOD = 10**9 + 1
values = set()
done = 0
for i in xrange(2,SIZE):
    newCount = [0]*len(count)
    for newElt in range(1,7):
        newCount[newElt] = sum(count[newElt:])
    for oldElt in range(1,len(count)-1):
        newCount[oldElt+1] += count[oldElt] * (7-oldElt)
    count = [x%MOD for x in newCount]
    a = tuple(count)

    
print sum(count)
print count


print "Time Taken:", time.time() - START

"""
Congratulations, the answer you gave to problem 458 is correct.

You are the 180th person to have solved this problem.

Return to Problems page.

OMG WOW... I feel kinda lame LOL... we just went over this algorithm in my 174 class and I didn't learn it then. Well, this is a lesson to me, use fast matrix exponentiation to solve it.

The way I did it (which works too, but is kinda less cool) is that I noted which letters we could add at each stage without creating a permutation of 'product', and kept track of how many unique letters we had in the last 6 so far. Then I looked at it and realized it repeated so i got rid of my excess work and just realized I only needed it to a certain step, aka, 2.5 * 10**8... which is huge, but not too bad since I ran it in C++ xP...

"""
