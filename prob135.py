import time
START = time.time()

size = 10**6
numbers = dict()
count = 0

for a in xrange(1,10**6):
    for b in xrange(a/4+1,a):
        num = (4*b-a)*a
        if 0 < num < size:
            if num in numbers:
                numbers[num] +=1
            else:
                numbers[num] = 1
        else:
            break

print "Time Taken:", time.time() - START

for i in xrange(1,10**6):
    if i in numbers and numbers[i] == 10:
        count +=1

print count
print "Time Taken:", time.time() - START


"""
~/Desktop/python_projects/proj_euler $python prob135.py
4989
time elapsed = 2.11237287521

If we consider the numbers to be in a decreasing arithmetic sequnce, then we can represent them as:
a+b,a,a-b.

We know that since (a+b)^2 > a^2 + (a-b)^2, we directly get
a^2+2ab+b^2 > a^2 + a^2 - 2ab + b^2 -->
4ab > a^2 -->
4b > a --> b > a/4

Additionally, we know that since we're representing the numbers as such, a > b otherwise we have negative numbers in the sequence.

Luckily enough, using a+b,a,a-b, we get that:
(a+b)^2-a^2-(a-b)^2 = 4ab - a^2 = 4(b-a)a = n. This simplifies calculations very much, and using this, we can know when to stop, aka when we hit an 'a' such that a > size.


Pretty cool problem~ (my 153rd one solved :D )
"""
