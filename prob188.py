import time
START = time.time()


powz = 1777
for i in range(0,1854):
  powz = pow(1777,powz,10**6)

print "The answer is:", pow(1777,powz,10**8)

print "Time Taken:", time.time()-START


"""
The answer is: 95962097
Time Taken: 0.00172019004822 

"""
