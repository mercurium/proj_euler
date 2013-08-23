import time
START = time.time()

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
				#print first_num, second_num, last_num
				count +=1

print "count was", count



print "Time Taken:", time.time() - START

"""
Congratulations, the answer you gave to problem 109 is correct.

You are the 3650th person to have solved this problem.

count was 38182
Time Taken: 0.0144000053406
"""
