#NOTE TODO need to solve it
import string

SIZE      = 30 + 2
NUM_BELLS = 1
ta        = [[1.0] * SIZE for x in range(SIZE) ]
ta2       = [[1.0] * SIZE for x in range(SIZE) ]

def probEV(prevNum, expectedNumHalf, expectedNumThird, expectedNumFourth):
  # TODO figure this out for more than one case.
  return 0

expected = 1
for i in xrange(1, SIZE-1):
  for j in xrange(1,SIZE-1):
    chance = 4
    if i == 1 or i == SIZE-2:
      chance -= 1
    if j == 1 or j == SIZE-2:
      chance -= 1
    ta2[i-1][j] *= (1 - ta[i][j]/chance)
    ta2[i+1][j] *= (1 - ta[i][j]/chance)
    ta2[i][j-1] *= (1 - ta[i][j]/chance)
    ta2[i][j+1] *= (1 - ta[i][j]/chance)

print sum([sum(x) for x in ta2[1:31]][1:31])

"""
for numloops in xrange(0,NUM_BELLS):
  # adding an extra one column/row before /after grid so I can avoid bounds checking
  for i in xrange(1, SIZE-1):
    for j in xrange(1,SIZE-1):
      chance = 4
      if i == 1 or i == SIZE-2:
        chance -= 1
      if j == 1 or j == SIZE-2:
        chance -= 1
      ta2[i-1][j] += ta[i][j]/chance
      ta2[i+1][j] += ta[i][j]/chance
      ta2[i][j-1] += ta[i][j]/chance
      ta2[i][j+1] += ta[i][j]/chance
  ta  = ta2
  ta2 = [[0.0] * SIZE for x in range(SIZE) ]

sumz = 0
for i in xrange(1, SIZE-1):
  for j in xrange(1,SIZE-1):
      sumz +=1 -ta2[i][j]
print sumz
"""








