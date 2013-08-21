import string
import time

START = time.time()
max_value = 0
for i in range(9236,9500):
	next_num = str(i) + str(i*2)
	if string.join(sorted(next_num),'') == '123456789':
		print i, 2*i
		if int(next_num) > max_value:
			max_value = next_num

print "The answer was:", max_value
print "Time Taken:", time.time() - START
