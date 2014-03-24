import time, string
from itertools import product
START = time.time()
SIZE = 10**4

values = [0,1,2] + [0] * (SIZE -2)
num_left = set(range(1,SIZE+1))

values[9999] = 11112222222222222222
values[999] = 111222222222222
values[999*2] = values[999]
values[9990] = values[999] * 10
values[999*5] = values[999] * 10

num_dig = 1
while len(num_left) != 0:
    for i in product("012", repeat=num_dig):

        for dig in '12':
            num = int(dig+string.join(i,""))
            if num == 0:
                continue
            for j in num_left:
                if num % j == 0:
                    if values[j] == 0:
                        values[j] = num
                    else:
                        values[j] = min(num, values[j])


    for i in range(1,SIZE+1):
        if values[i] != 0:
            num_left.discard(i)
    num_dig+=1
    print num_dig+1, len(num_left)
    if len(num_left) < 50:
        print sorted(num_left)

print sum([values[i]/i for i in range(1,len(values))])
print "Time elapsed:", time.time() - START


"""
For this problem, I just iterated through different numbers 0, 1,2,10,11,12, etc, until I got the numbers. I just checked the numbers that weren't matched up yet so that it would be a bit faster. I was a bit annoyed at the speed so I just computed the values for 9999 and 9990 since it would have taken much longer otherwise (I'm not sure of the formula for the general number so I didn't do it that way)

1111981904675169
Time elapsed: 479.165813923

Congratulations, the answer you gave to problem 303 is correct.

You are the 1901st person to have solved this problem.

Return to Problems page.

"""
