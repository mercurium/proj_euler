import time
START = time.time()

s = [0] * (4*10**6)
for k in range(55):
	s[k] = (10**5+3 - (2*10**5+3) *(k+1) + (3*10**5+7) * (k+1)**3) % 10**6 - 500000
for k in range(55,len(s)):
	s[k] = (s[k-24] + s[k-55])%10**6 - 500000

max_sum = 0

for j in range(2000):  #rows
	row = s[j*2000:(j+1)*2000]
	cumm_sum = 0
	for i in row:
		cumm_sum += i
		if cumm_sum < 0:
			cumm_sum = 0
			continue
		if cumm_sum > max_sum:
			max_sum = cumm_sum

for j in range(2000): #columns
	col = s[j::2000]
	cumm_sum = 0
	for i in col:
		cumm_sum += i
		if cumm_sum < 0:
			cumm_sum = 0
			continue
		if cumm_sum > max_sum:
			max_sum = cumm_sum

print max_sum
print "Time Taken:", time.time() - START

"""
Congratulations, the answer you gave to problem 149 is correct.

You are the 2456th person to have solved this problem.

"""
