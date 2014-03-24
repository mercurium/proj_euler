import time
start = time.time()
from bitarray import bitarray

SIZE = 10**7*2
LOWER_BOUND = 10**7


def get_primes(size):
    prime_lst = bitarray('000' + '01' * (size/2-1))
    for i in xrange(3,size,2):
        if prime_lst[i] == 0:
            for j in xrange(i**2,size,2*i):
                prime_lst[j] = 1
    return prime_lst

def dig_root(num):
    if num < 10:
        return 0
    return sum(int(x) for x in str(num))

def max_clock(old,new):
    if new == 0: #if we're done, just turn off all numbers.
        return sum([lc[int(x)] for x in str(old)])
    old,new = str(old),str(new)
    sumz = sum([ lc[int(x)] for x in old[:(len(old) -len(new))] ])
    old = old[len(old)-len(new):]
    for i in xrange(len(new)):
        sumz += nd[int(old[i])][int(new[i])]
    return sumz

def sam_clock(old,new):
    if new == 0:
        return sum([lc[int(x)] for x in str(old)])
    return sum([ lc[int(x)] for x in (str(old)+str(new)) ])    

num_set = [0]*10
num_set[0] = set([1,2,3,4,5,7])
num_set[1] = set([3,4])
num_set[2] = set([2,3,5,6,7])
num_set[3] = set([3,4,5,6,7])
num_set[4] = set([1,3,4,6])
num_set[5] = set([1,4,5,6,7])
num_set[6] = set([1,2,4,5,6,7])
num_set[7] = set([1,3,4,5])
num_set[8] = set([1,2,3,4,5,6,7])
num_set[9] = set([1,3,4,5,6,7])

letter_count = [6,2,5,5,4,5,6,4,7,6]
lc = letter_count

nd = [0]*10 #setting up the differences between changing numbers
for i in range(len(nd)):
    nd[i] = [0]*10
    for j in xrange(len(nd[i])):
        nd[i][j] = len(num_set[i].symmetric_difference(num_set[j]))

#########################################################
############ABOVE THIS IS JUST SETUP ####################
#########################################################

max_sum, sam_sum = 0,0
plst = get_primes(SIZE)
for i in xrange(LOWER_BOUND,SIZE):
    if i %1024 == 0:
        print i
     if plst[i] == 1:
         continue
    old,new = i, dig_root(i)
    max_sum += max_clock(old,0)
    sam_sum += sam_clock(old,0)
    while new != 0:
        max_sum += max_clock(old,new)
        sam_sum += sam_clock(old,new)
        old,new = new, dig_root(new)
    max_sum += max_clock(old,0)
    sam_sum += sam_clock(old,0)
    
print "sam's sum is:", sam_sum
print "max's sum is:", max_sum
print "Diff is:", sam_sum - max_sum
print "Time Taken:", time.time() - start

"""
Congratulations, the answer you gave to problem 315 is correct.

You are the 1228th person to have solved this problem.

okay, the math behind this... it wasn't particularly a hard problem really, I was just too lazy to do it earlier. So for the variables, num_set is the set of dashes that each number has. letter count is the length of each of those sets in num_set, nd = number_difference is the difference in dashes between each of the 10 digit. Only useful for max's clock.

For the computation, I had a dig_root function that turned a number into its digital root...
For Sam, I just appended the two numbers and computed the cost of turning old off and new on.
For max, I used the list of numbers that I computed earlier that tells how much they have changed to see their difference. Nothing too complicated in either of them... :x


sam's sum is: 63424722
max's sum is: 49799480
Diff is: 13625242
Time Taken: 36.3213140965
Time Taken: 30.7954418659 (not sure what I changed... ._.)
"""
