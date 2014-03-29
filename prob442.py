#NOTE TODO need to solve it
import time, math
START = time.time()

count = [1,10]

for dig in range(2,19):
	temp_count = 0
	for dig_len in range(2,dig+1):
		for start in range(0, dig- dig_len+1):
			temp_count += count[start] * (10**(dig-start-dig_len)- \
				sum([10**x for x in range(dig-start-dig_len)]))
	
	count.append(9* 10**(dig-1) -temp_count +count[-1])

print count
print count[-1], 10**18-count[-1], math.log(10**18-count[-1],10)
print "time taken:", time.time() - START

print "okay, so that's the majority of them, now for the rest..."





"""
19:35 ~/Desktop/python_projects/proj_euler $ python prob442.py                                                        
[1, 10, 99, 979, 9681, 95734, 946705, 9361892, 92579038, 915507091, 9053380277, 89528191841, 885337508138, 8755035561431, 86577883549894, 856162132910112, 8466522485580903, 83724799595140123, 827948201777605653] 
827948201777605653 172051798222394347 17.2356592161
time taken: 0.00135016441345 
okay, so that's the majority of them, now for the rest... 
"""
