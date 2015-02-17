import time
START       = time.time()

SIZE        = 10**6
previousVal = (SIZE+1)/2.0

for i in xrange(SIZE-1,0,-1):
  costToEnd    = (SIZE +1) / ( i + 1.0 )

  numBigger    = previousVal // costToEnd
  numSmaller   = i - numBigger

  decreaseMult = numBigger * (numBigger + 1) / 2
  decreaseVal  = decreaseMult * costToEnd

  sameVal      = numSmaller * previousVal
  previousVal  = ( decreaseVal + sameVal ) / i


print "The answer is:", previousVal
print "Time Taken:", time.time() - START


"""

Congratulations, the answer you gave to problem 503 is correct.

You are the 60th person to have solved this problem.

The answer is: 3.86945501449
Time Taken: 1.24571895599
Time Taken: 1.10621595383 (removed an excess multiplication)
Time Taken: 0.980906009674 (removed the function call)
Time Taken: 0.921088933945 (turned an int cast into a // )
Time Taken: 0.888251781464 (turned a float into an int)

"""
