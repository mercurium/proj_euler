import time
START = time.time()

n = 290797
MOD = 50515093
SIZE = 10**4

sumz = 0
min_val = [0] * 50 # (value, index)
next_val = (n**2)% MOD
index = 0
for i in xrange(SIZE):
    for j in xrange(0,index):
        if min_val[j][0] > next_val:
            index = j
            break
    min_val[index] = (next_val,i)
    index +=1

    for num in xrange(index-1,0,-1):
        sumz += min_val[num][0] * (min_val[num][1] - min_val[num-1][1])
    sumz += min_val[0][0] * (min_val[0][1]+1)
    print i,sumz
    next_val = (next_val**2)%MOD


print sumz
print "Time Taken:", time.time() - START

"""
Congratulations, the answer you gave to problem 375 is correct.

You are the 425th person to have solved this problem.

Return to Problems page.

solved it using c++ for efficiency reasons ;P
"""
