"""

Okay, so I didn't actually need to write a program for this one, but I'm writing this down so I can use this as reference later.

I noticed early on that it was pretty easy to figure out which numbers had int powers. After all, it was just 4^x = 2^x + a where we have x = 1,2,3,... 

Then I realized somewhere along the way that the only solutions (a) to this are where a = b*(b+1) for some integer b.

The reasoning behind this can be explained by:
4^x = 2^x +a
--> 4^x -2^x = a
--> 2^x(2^x-1) = a
If we let b = 2^x, then we get
a = b*(b-1). Since 2^x can be equal to any positive real number >= 1 if x >= 0, the only problem is finding an a = b*(b-1)

So we have the method of finding # of ones that are integers and the number of ones that are just real numbers.

The next lazy step i took was:

def g(n): return 2**i * (2**i -1)
def f(n): return (12345*n)*(12345*n+1)

for i in xrange(30,1,-1):
  if f(n) > g(n):
    print n
    break

This gives us n= 17, which means that if we plug in
(12345*17+1)*(12345*17+2), we get our answer, which happens to be
44043947822

"""
