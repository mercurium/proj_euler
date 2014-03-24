import time
start = time.time()

SIZE = 10**4
LIM = 4*10**6


pfactor = range(SIZE)
for i in xrange(4,SIZE,2):
    pfactor[i] = 2
for i in xrange(3,SIZE,2):
    if pfactor[i] == i:
        for j in xrange(i**2,SIZE,2*i):
            pfactor[j] = i

def factor(n):
    factors = []
    while n > 1:
        factors.append(pfactor[n])
        n /= pfactor[n]
    return sorted(factors)

maxz = 0
for num in xrange(1,SIZE):
    if num == pfactor[num]:
        continue
    factors = factor(num)
    factor_map = dict()
    factor_set = set(factors + [2,3,5,7,11,13,17,19,23,29])
    factor_map[2] = 7   #These are just forcing the number to have these values to save time...
    factor_map[3] = 7
    factor_map[5] = 5
    factor_map[7] = 5
    factor_map[11] = 3
    factor_map[13] = 3
    factor_map[17] = 3
    factor_map[19] = 3
    factor_map[23] = 3
    factor_map[29] = 3
    for f in factors:
        if f not in factor_map:
            factor_map[f] = 3
        else:
            factor_map[f] +=2    
    prod = 1
    numz = 1
    for f in factor_set:
        prod *= factor_map[f]
        numz *= f**(factor_map[f]-1)
    if prod/2 >= LIM:
        print prod, int(numz**.5), "DONE!!!"
        break
    if prod > maxz: #for benchmarking...
        maxz = prod
        print maxz, int(numz**.5)

print "Well, the biggest we saw was:", maxz 
print "Time Taken:", time.time() - start


"""
Congratulations, the answer you gave to problem 110 is correct.
You are the 4034th person to have solved this problem.

8037225 9350130049860600
^ is the number of factors, 935... is the number that gives this many factors, its prime factoriazion is... 
[2, 2, 2, 3, 3, 3, 5, 5, 7, 7, 11, 13, 17, 19, 23, 29, 31, 37, 1]

anyways... for this problem and 108, I figured out that if 1/x + 1/y = 1/z, then...
=> x + y = xy/z
=> xz + yz = xy
=> xy - xz - yz = 0
=> (x-z)(y-z) = z^2
Which means we just need to find the number z such that z^2 has SIZE*2 factors.
...yeah. after that, rest was easy :x.
I used the factor mapping addition to make it so that we didn't have to iterate that high since we knew that we wanted to use those factors for sure anyways... :x..



"""
