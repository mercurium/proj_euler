import time
from math import sqrt, log
START = time.time()

squares = set([x**2 for x in xrange(1,10**5)])

"""
squares:
x-y = a 
x+y = a+2b+2c
x-z = a+b
x+z = a+b+2c
y-z = b
y+z = b+2c

so a,b, a+b are triangle numbers squared...
"""

found_ans = False
x,y,z = 0,0,0
for m in xrange(1,1000):
    for n in xrange(1,m):
        for k in xrange(1,20): #Generic method for generating pythagorean triples.
            a,b = (m**2 - n**2)**2*k**2 , 4 * m**2 * n**2*k**2 #We want the squares of it, so we know that a+b is a square too.
            for mult in xrange(2,10**6,2):
                c = 4*m*n*mult * k + mult**2  #We guarentee that b+c is a square like this. c is explicitly constructed such that this is so.
                if c/40 > b: #If c gets too big, it's probably not right.
                    break
                if (a+b+c) in squares and (a+2*b+c) in squares:
                    c /=2
                    print a,b,c
                    x,y,z = a+b+c, b+c,c
                    found_ans = True
            if found_ans: break
        if found_ans: break
    if found_ans: break

print "The three numbers are:", x,y,z #because i'm pretty darn curious what the three numbers are..
print "Their sum is:", x+y+z
print "Time Taken:", time.time() - START

print (x+y)**.5, (x-y)**.5  #These three prints are to double check the answer
print (x+z)**.5, (x-z)**.5
print (y+z)**.5, (y-z)**.5

"""
a = x-y
b = y-z
c = z

squares:
x-y = a 
x+y = a+2b+2c
x-z = a+b
x+z = a+b+2c
y-z = b
y+z = b+2c

Congratulations, the answer you gave to problem 142 is correct.

You are the 2877th person to have solved this problem.

Return to Problems page.


13689 270400 150568
The three numbers are: 434657 420968 150568
Their sum is: 1006193
Time Taken: 0.0674960613251
925.0 117.0
765.0 533.0
756.0 520.0


Okay, cool. So first off, I decided heyyyy, we're only dealing with three variables here (x,y,z), let's meddle with them a bit to get the requirements down.
So I decided why not let 'a = x-y', 'b=y-z', and 'c =z'. Then this means that we need to have the 6 following equations be squares:
a (x-y)
a+b (x-z)
b (y-z)
a+2b+2c (x+y)
a+b+2c (x+z)
b+2c (y+z)

Then I noticed that since the triplet (a,b,a+b) have to be squares, we can generate them using the method for finding pythagorean triples, ( http://en.wikipedia.org/wiki/Pythagorean_triple#Generating_a_triple if you need it).
Using this, I instantly got 3 of the six equations to be squares for free. Next, by setting c such that b + 2c is always a square by choosing the values of 'c' wisely, the only two squares I had left to check were
a+2b+2c and a+b+2c. This didn't take much work and as a rsult, I managed to get my answer in Time Taken: 0.0673670768738... not bad ;)


############################### OLD REASONING BELOW:



a^2 = x+y
b^2 = x-y
c^2 = x+z
d^2 = x-z
e^2 = y+z
f^2 = y-z
a^2+b^2 = c^2+d^2
b^2+f^2 = d^2
b^2+e^2 = c^2
b^2+e^2+f^2 = a^2


OR

x+y = (n+a)^2
x-y = (n-a)^2
x = n^2 + a^2
y = 2an

y+z = (m+b)^2
y-z = (m-b)^2
y = m^2 + b^2
z = 2mb

x+z = (p+c)^2
x-z = (p-c)^2
x = p^2+c^2
z = 2pc

So from the previous statements...

x = n^2+a^2 = p^2+c^2
y = m^2+b^2 = 2an
z = 2mb = 2pc


"""

