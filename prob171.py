import time
start = time.time()

DIGITS = 20

vals = dict()
sum_vals = dict()
for i in xrange(10):
    vals[i**2] = 1
    sum_vals[i**2] = i
squares = set([x**2 for x in range(1,41)])
sumz = 0
############################### setup is before this point.

for i in xrange(1,DIGITS):
    sumz = 0
    for key in vals.keys():
        if key in squares:
            sumz += sum_vals[key]
    print sumz
    
    new_vals = dict()
    new_sum_vals = dict()
    for key in vals.keys():
        for j in xrange(0,10):
            if (key+j**2) in new_vals:
                new_vals[key+j**2] += vals[key]
                new_sum_vals[key+j**2] += 10**i*j*vals[key] +sum_vals[key]
            else:
                new_vals[key+j**2] = vals[key]
                new_sum_vals[key+j**2] = 10**i*j*vals[key] +sum_vals[key]
    vals = new_vals
    sum_vals = new_sum_vals


sumz = 0
for key in vals.keys():
    if key in squares:
        sumz += sum_vals[key]
print sumz

print "Final answer is:", sumz %10**9
print "Time Taken:", time.time() - start

"""
Problem isn't too bad, just need to keep track of 

Congratulations, the answer you gave to problem 171 is correct.

You are the 1304th person to have solved this problem.

Return to Problems page.

Output is:
20:58 ~/Desktop/python_projects/proj_euler $ python prob171.py 
45
726
28083
1719828
161887270
16608872280
1782587599519
175563709355474
16744183205478039
1542720102067950212
142168514031911648193
13364169620764413608157
1283365898693204996743464
124634234586076531435431917
12132951874162987867048125837
1178942729365307659883504841247
114344197095063654412113584604919
11088639937600804544466915617954751
1077037710100447177670074006767733060
104861799630145516743395826448142989277
Final answer is: 142989277
Time Taken: 0.170722007751
"""

