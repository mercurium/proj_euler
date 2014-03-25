import time
START = time.time()

start, end = 10**6, 10**6+10**5

for num in xrange(start, end):
    if num % 2 == 0 or num %5 == 0: #Not going to be a repunit
        continue
    print num
    done = True
    sumz = 1
    for powz in xrange(1, 10**6+1):
        sumz = (sumz + pow(10,powz,num))% num
        if sumz == 0:    
            done = False
            break

    if done:
        print num, 'DONE'
        break    

print "Time Taken:", time.time()-START
