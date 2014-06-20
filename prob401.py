import time
START = time.time()

SIZE = 10**15 
MOD  = 10**9 
count = 0  #Our accumulator variable

#Formula here: http://en.wikipedia.org/wiki/Square_pyramidal_number
def sumSq(n): 
    return n*(n+1) *(2*n+1)/6

def accountForLargeNumbers(size, lim):
    count = 0
    for d in xrange(1,lim+1):
        n = size/d
        count += sumSq(n)
    return count

def accountForSmallNumbers(size,lim):
    count = 0 
    numbersAlreadyCounted = size/lim
    for d in xrange(1, lim):
        count += (size/d - numbersAlreadyCounted ) * d**2
    return count

def main():
    largeNumSum = accountForLargeNumbers(SIZE, 10**7*2)
    smallNumSum = accountForSmallNumbers(SIZE, 10**7*5)
    print "The answer is:", (largeNumSum + smallNumSum) % MOD
    print "Time Taken:", time.time()-START

main()

"""
Congratulations, the answer you gave to problem 401 is correct.

You are the 1038th person to have solved this problem.

For this problem, there are (at least) two ways to count the sum of the squares of the divisors from 1 to N. 

The first way is to compute N/d, for every d up to N, and multiply it by d^2 for the divisors squared sum
The second way is to see how many squares occur once, occur twice, and etc. We then have from that the numbers from 1 to N/d occur at least d times.

Unfortunately, using either of these methods individually is slow (10^15 divisions anyone?), but surprisingly, combining the two allows us to reduce the problem size to something only a square root of the size. Since the two approaches come in from opposite sides (one is high to low, the other is low to high), we can use the one that is more efficient at each chunk, and thus do approximately 7 * 10^7 operations instead of 10^15.


First run:
~/proj_euler $python prob401.py
Time Taken: 7.84915804863 #first half
281632621
Time Taken: 47.5886650085 #total runtime

Upon restructuring the limits, I reduced it to:
Time Taken: 34.7627840042
And after removing the %MOD, and removing the function call, I get
Time Taken: 31.6589548588
but it's not worth keeping since it makes the code less readable and not that much faster

Okay, I'm not sure what I did but I somehow managed to get:
Time Taken: 20.8848359585
after I refactored / cleaned up the code a bit. So weird...

"""
