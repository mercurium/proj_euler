import time
START = time.time()

""" Initializing the possible points """
numbers = range(1,21) + [25]
doubles = range(2,42,2) + [50]
triples = range(3,63,3)

all_nums = sorted([0] + numbers + doubles + triples)

count = 0
for last_num in doubles:
    for second in range(len(all_nums)):
        second_num = all_nums[second]
        for first_num in all_nums[:second+1] :
            if first_num > second_num:
                break
            if last_num + second_num + first_num < 100:
                count +=1

print "count was", count



print "Time Taken:", time.time() - START

"""
Congratulations, the answer you gave to problem 109 is correct.

You are the 3650th person to have solved this problem.

count was 38182
Time Taken: 0.0144000053406


Okay, so since the final toss has to be a double, we can only consider the doubles for the last number, hence the first loop on line 12. After that, we iterate through all possible combinations of two other numbers. However, because D1 S2 D1 is the same as S2 D1 D1, we need to break symmetry and so we foce the first number to be smaller than the second (could have done other way around too, doesn't matter). Then, if the three numbers we have add up to < 100, then we're good and include it in our count. 

This problem wasn't very hard, I just avoided it for a while because I didn't like graphical problems... hehee.... should start getting used to them more...
"""
