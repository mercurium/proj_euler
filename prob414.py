#NOTE TODO need to solve it
import time
START = time.time()
BASE = 15

def kaprekarRoutine(lst, base):
    a = sorted(lst)[::-1]
    b = a[::-1]
    if a[0] == b[0]:
        return lst
    for j in range(len(a)-1,-1,-1):
        a[j] -= b[j]
        if a[j] < 0:
            a[j] += base
            a[j-1] -=1
    return a

countLst = [0]*40
for a in xrange(BASE):
    print a, countLst
    for b in xrange(BASE):
        print b
        for c in xrange(BASE):
            for d in xrange(BASE):
                for e in xrange(BASE):
                    count = 0
                    lst = [a,b,c,d,e]
                    nextLst = kaprekarRoutine(lst,BASE)
                    while lst != nextLst:
                        lst = nextLst
                        nextLst = kaprekarRoutine(lst,BASE)
                        count +=1
                        if count > 50:
                            print "ERROR!!!", [a,b,c,d,e]
                            break
                    countLst[count] +=1

print countLst, sum([x*countLst[x] for x in range(len(countLst))])

print "Time Taken:", time.time() - START
