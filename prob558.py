import time
START = time.time()

# Super simple binary search function
def binSearch(func, lowerBound, upperBound, target, error):
  mid = (lowerBound + upperBound) / 2.0
  result = func(mid)
  if result > target:
    return binSearch(func, lowerBound, (lowerBound + upperBound)/2, target, error)
  elif func(mid+error) < target:
    return binSearch(func, (lowerBound + upperBound)/2, upperBound, target, error)
  else:
    return mid


root = binSearch((lambda x: x**3 - x**2 - 1), 1.4, 1.5, 0, 10**-14)

r = root

print root, root**3 - root**2 - 1

print root**6 + root**-7

print r**2 - r


print "Time Taken:", time.time() - START


"""
do not have the level of precision to guestimate out the elements. Will need to use precise values

f(-10) = -3r^2 +  r + 5
f(-9)  = -2r^2 + 5r - 3
f(-8)  =  3r^2 + 5r - 2
f(-7)  =       - 2r + 3
f(-6)  = -2r^2 + 3r
f(-5)  =   r^2      - 2
f(-4)  =   r^2 - 2r + 1
f(-3)  =  -r^2 +  r + 1
f(-2)  =          r - 1
f(-1)  =   r^2 -  r
f(0)   =              1
f(1)   =          r
f(2)   =   r^2
f(3)   =   r^2 +    + 1
f(4)   =   r^2 +  r + 1
f(5)   =  2r^2 +  r + 1
f(6)   =  3r^2 +  r + 2

"""
