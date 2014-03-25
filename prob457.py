#NOTE TODO need to solve it

import time
START = time.time()
SIZE = 10**3
from primes import m_r

class Node:
    def __init__(self, value, nextVal):
        self.value = value
        self.next = nextVal

headNode = Node(2,None)
lastNode = headNode
pfactor = range(0,SIZE+1)
for i in xrange(2,len(pfactor)):
    if pfactor[i] == i:
        for j in xrange(i*2,len(pfactor),i):
            pfactor[j] = i
        lastNode.next = Node(i, None)
        lastNode = lastNode.next
headNode = headNode.next

print "Time Taken: ", time.time() - START
sumz,count = 0, 0
answer = [0] * (SIZE+1)



for i in xrange(4,SIZE+1):
    if i %512 == 0:
        print i, count, "Time Taken:", time.time() - START


    nextNum = (i*i - 3*i-1)
    if m_r( nextNum):
        continue
    currentNode = headNode
    prevNode = None

    while currentNode.next != None:
        if currentNode.value < i:
            headNode = currentNode.next
            currentNode = currentNode.next
            continue
        if currentNode.value > nextNum:
            break
        if nextNum % currentNode.value == 0:
            answer[currentNode.value] = i
            if prevNode == None:
                headNode = currentNode.next
            else:
                prevNode.next = currentNode.next
            currentNode = currentNode.next
            count +=1
        else:
            prevNode = currentNode
            currentNode = currentNode.next

"""
for i in xrange(len(answer)):
    if answer[i] != 0:
        print i, answer[i]
"""
print sum(answer)
print "Time Taken: ", time.time() - START


"""
iterCount1,iterCount2 = 0,0
primeCount = 0
worksCount = 0
notWorking = []
for p in xrange(2,SIZE):
    if p% 1024 == 0:
        print p, sumz, iterCount1, iterCount2, worksCount, primeCount
    if pfactor[p] == p:
        primeCount +=1
        x = -1
        for i in xrange(1,p/2+1):
            iterCount1+=1
            if (i**2-3*i-1) % p == 0:
                x = i
                break
        if x == -1:
            notWorking.append(p)
            continue
        y = p-x+3
        worksCount +=1
        for j in xrange(0,p/2+2):
            iterCount2 +=1
            a,b = j*p+x, j*p+y
            if (a**2-3*a-1) % p**2 == 0:
                sumz += a
                print p, a, sumz, a * 1.0 / p**2
                break
            if (b**2-3*b-1) % p**2 == 0:
                sumz += b
                print p, b, sumz, b * 1.0/p**2
                break
print sumz
print "Time Taken: ", time.time() - START
print "took", iterCount1, iterCount2, "iterations"
print "Only", worksCount, "out of ", primeCount, "had this work"
print "The ones we should have skipped were:", notWorking


"""
