import time
START = time.time()

val_list = []
for i in xrange(37):
    val_list.append([])

for i in xrange(10**4):
    a,b,c,d = i/1000, (i/100)%10, (i/10)%10, i%10
    n = a+b+c+d
    val_list[n].append([a,b,c,d])

count = 0
for val in range(19):
    for i in val_list[val]:
        for j in val_list[val]:
            for a in range(10):
                if i[0] + j[0] + a > val or i[1] + j[2] + a > val:
                    break
                b = val - i[0] - j[0] - a
                c = val - i[1] - j[2] - a
                d = val - i[3] - j[3] - c
                if d != val - i[2] - j[1] - b or b > 9 or c > 9 or d > 9:
                    continue
                for e in range(10):
                    if i[1] + j[1] + e > val or i[0] + j[3] + e > val:
                        break
                    g = val - i[1] - j[1] - e
                    f = val - i[0] - j[3] - e
                    h = val - j[2] - i[2] - f
                    if h != val - g - i[3] - j[0]:
                        continue
                    if min([a,b,c,d,e,f,g,h]) >= 0 and max([a,b,c,d,e,f,g,h]) <= 9:
                        if val < 18:
                            count +=1
                        count +=1
    print val, len(val_list[val]),count, time.time()  -START
    
print count

print "Time Taken:", time.time() - START


"""
For this problem, there are 10^16 possible grids. Obviously, this is too much to check so I tried to figure out ways to trim down the search space. First off, we only need to check grids where all rows have the same sum. This can be done by sorting out the rows to lists so that we only grab rows with equivalent sums. This reduces the overall computation to approximately... 10^12.18, which IS much better than 10^16 but still bad.

Then, if you consider that if you know three rows, you can fill in the remaining row, we can then reduce the computation to ~10^9.42 cases to check. 

THEN!!! If we decide instead that the two rows we want to fill in are the diagonals, then we can make it so that there are:
    row * row * num * num      choices instead ~= 10^8.68 as an UPPER limit.

If we have two rows for each number, (i and j), if we pick 'a' and 'e' and know what they sum up to, we can determine the rest of the grid. Since the choices of 'a' and 'e' don't always go from 0-9, we can safely do less than 10^8.68 computations, saving us a lot of time.
i0  a  b j0
e  i1 j1  g
f  j2 i2  h
j3  c  d i3

One last trick, is that if we took 9-x for every entry x in the matrix, we'd have another solution, we can safely double each answer and save ourselves half the computing time, reducing the actual hard limit to:

~10^8.339 ~= 200 million.

YAY MATH

Congratulations, the answer you gave to problem 166 is correct.

You are the 2160th person to have solved this problem.
7130034
Time Taken: 86.9943490028  
Time Taken: 38.4768619537  (after getting rid of half the redundant computation)
Time Taken: 30.6089820862  (removing excess checking)
"""
