import time, math
START = time.time()
SIZE = 3**37

memoizedVals = {0:0,1:1, 3:3}
def f(n): #The definition of the function from the problem statement
    if n in memoizedVals:
        return memoizedVals[n]
    if n % 2 == 0:
        memoizedVals[n] = f(n/2)
    elif n%4 == 1:
        memoizedVals[n] = 2*f(n/2+1) - f(n/4)
    else: #if n%4 == 3
        memoizedVals[n] = 3*f(n/2) - 2* f(n/4)
    return memoizedVals[n]
    
sumz = 5 # f(1) + f(2) + f(3)
index = 4
ABdict = dict()
ABdict[4] = (6,2)

while index*2 < SIZE:
    a,b = ABdict[index]
    sumz += index**2
    ABdict[index*2] = (5 * a - b, 3 * a + b)
    index *=2

while index <= SIZE:
    if SIZE - index < 10: #end case, don't want to deal with it specially
        sumz += sum([f(i) for i in range(index, SIZE+1)]) #so we just compute f(x) for these values
        break

    nextPow = int(math.log(SIZE-index, 2)) #the largest power of 2 smaller than diff(Size,index)
    nextChunk = 2**nextPow

    n = index / nextChunk 
    a,b = ABdict[nextChunk]
    sumz += a*f(2*n+1) - b*f(2*n)
    index += nextChunk

print "The Answer is:", sumz % 10**9
print "Time Taken:", time.time() - START

"""
Congratulations, the answer you gave to problem 463 is correct.
You are the 307th person to have solved this problem.

The Answer is: 808981553
Time Taken: 0.000306129455566

Okay, cool, solved it :D. So, the main insight I had with this problem was that it's possible to simplify the sum into chunks of powers of two.
Ex: sum from 1 to 100 =  (let s(a,b) = sum from a to b-1)
s(1,63) + s(64, 95) + s(96,99) + f(100)

I didn't find this out until later, but it turns out that s(2^n, 2^(n+1)) = 2^(2n) ...I wonder why :o

Anyways, I computed s(1,3) by hand (oh noes), then turned the problem into
s(1,3) + s(4,7) + s(8,15) + s(16,31) + s(32,63) + s(64,95) + s(96,99) + f(100)

The reason for this is that my equation for s(k * n, k * n + 2^j - 1) (2^j < k) doesn't work when k = 0... sigh limitations xD)

Anywhoo, so I figured out that:
    f(4n) + f(4n+1) + f(4n+2) + f(4n+3) = 6 f(2n+1) - 2f(2n)
and:
    a * f(4n+1) - b f(n) +
    a * f(4n+3) - b f(2n+1) =

    (5a - b) f(2n+1) - (3a+b) f(n)

Using these two equations, and dividing up the summation into segments, I just had to plug it in and then I got the answer. Yay!


"""
