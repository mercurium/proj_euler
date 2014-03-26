import time
START = time.time()
SIZE = 10**12

def gcd(a,b):
    while a!= 0:
        a,b = b%a,a
    return b


sumz = 0
for a in xrange(1,int(SIZE**.5)):
    for b in xrange(1, int((SIZE/a**2)**(1/3.))):
        for c in xrange(1,min(SIZE/(a**2 * b**3)+1,b)):
            num = a**2 * b**3 * c + a*c**2
            if num > SIZE:
                break
            if gcd(b,c) != 1:
                continue
            if int(num**(1/2.))**2 == num:
                sumz += num
                print num, a,b, c

print sumz
print "Time Taken:", time.time() - START

"""
number = ab^2 * (abc) + ac^2 = a^2b^3c + ac^2

Congratulations, the answer you gave to problem 141 is correct.

You are the 1941st person to have solved this problem.

Return to Problems page.

878454337159
Time Taken: 17.0076379776

Basically, if three numbers are part of a geometric sequence, we can represent them as:

ab^2, abc, ac^2, with a = constat multiple, and b/c being the geometric factor...

so just have n = (ab^2)(abc) + ac^2, and check for all valid a,b,c, keeping in mind b > c.
Then, upon getting n, just check to make sure it's a square. Hurr durr.. spent too much time making sure that n was a square when i could just do a simple check later T.T...


"""
