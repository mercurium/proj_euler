import time
START = time.time()

for loop in range(111,999):
    if loop % 10 == 0 or loop / 10 % 10 == 0:
        continue
    # i,j,k = loop/100, loop/10 %10, loop %10
    if (loop/10) * (loop%10) == (loop/100) * (loop %100)  and loop % 10 != loop /100:
        print loop/10, loop %100 
    
                 
print "Time Taken:", time.time() - START
