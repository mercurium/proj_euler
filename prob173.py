import math
import time
start = time.time()
n = 10**6



count = 0
square_diff = 2
while (n - square_diff**2)/(2*square_diff) > 0:
	count = count + (n - square_diff**2)/(2*square_diff)
	square_diff = square_diff +2


print count
print "Time Taken:", time.time() - start
"""
22:38 ~/Desktop/python_projects/proj_euler $ python prob173.py 
1572729
Time Taken: 0.000257968902588

The basis for this question can be explained as such, each lamina is a square with an inner square removed.
As such, we can represent the number of squares as n^2 - (n-k)^2 = n^2 - n^2 +2nk -k^2 = 2nk - k^2 = k(2n - k)

OKAY. SOOO.... 

If we consider the squares of type (n-2)^2 and n^2, they differ by 4n +4. This means that the largest laminae formed by a pair of squares 2 apart is such that
4n - 4 <= 10^6. Obviously, this means that all other smaller squares work. As such, this is what we're measuring in the while loop.

For example, if n = 10^6, square_diff = 2, then there are 999996/(4) = 249999 different pairs that satisfy this requirement. This can be seen by noting that the largest n for which n, (n-2) form a laminae of size <= 10^6 is when n = 250,001, and the smallest pair for which n,n-2 satisfies it is 3 and 1. As a result, there are 249,999 numbers that work for a diff of 2 between the squares.

Applying the same logic to diffs of 4, diffs of 6, diffs of 8, etc, we get the answer we desire, which is 1,572,729

"""
