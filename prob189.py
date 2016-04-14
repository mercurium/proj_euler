import time
START = time.time()
from itertools import product

def minNoErr(setz):
  if len(setz) == 0:
    return 1000
  return min(setz)

# Some tuples are isomorphic, like (1,1,1) and (2,2,2), which means it helps to find a lower isomorphic tuple.
def getLowerEquiv(tupl):
  lst = [set(), set(), set()]

  for i in range(len(tupl)): #Getting the sets of all positions of the 1's, 2's, and 3's
    lst[int(tupl[i])-1].add(i)

  lst = sorted(lst, (lambda x, y: minNoErr(x) - minNoErr(y))) #Place the 1's first.

  ans = [0] * len(tupl)
  for i in range(3):
    for a in lst[i]:
      ans[a] = str(i+1)

  return tuple(ans)


valCount = {('1',):1, ('2',):1, ('3',):1}
for row in range(2,9):
  rowOverall = 0
  for combo in product('123', repeat=row): #tricoloring the triangle

    lowerEquiv = getLowerEquiv(combo) #We can skip some steps due to symmetry
    if lowerEquiv != combo: #This part saves us a LOT of work
      valCount[combo] = valCount[lowerEquiv]
    else:
      valCount[combo] = 0

      for oldCombo in product('123', repeat=row-1):
        currentCount = valCount[oldCombo]
        for spot in range(len(combo)-1):
          currentCount *= (3 - len(set([oldCombo[spot], combo[spot], combo[spot+1]])))
        valCount[combo] += currentCount

    rowOverall += valCount[combo]
  print row, rowOverall

print "Time Taken:", time.time() - START

"""

Congratulations, the answer you gave to problem 189 is correct.

You are the 1146th person to have solved this problem.

10834893628237824
Time Taken: 80.9676380157
Time Taken: 19.9419779778 once I accounted for symmetry at the last level
Time Taken: 13.6176569462 once I accounted for symmetry through the whole problem

Okay, so this problem is a Constraint Satisfiability Problem (CSP), and one of the generic strategies for these types of problems is to split the problem up into many independent problems with minimal dependencies.

Apologies in advance for the horrible ASCII art :P. For the example, I'm going to solve a triangle of height 3, with 9 triangles.

      /_\
    /_\_/_\  <--- This thing.
  /_\_/_\_/_\

      /1\
    /2\3/4\   #Pretend this is still a 9 part triangle :D;
  /5\6/7\8/9\

Anyways, so for this triangle, 6's color depends only on the mini triangles 2,5, and 7, and 8 depends on 4,7, and 9.
Thus, if we try all combos 1-4, 5,7, and 9, we can pretty easily figure out the number of valid 6 and 8 values.

Since 1-4 are the previous height's counts (and inside that, only 2/4 matter), we can build up our triangle incrementally, and so, trying all values of 2,4,5,7,and 9, and summing over those, we get the total number of height=3 triangles.

Repeating this all the way to height=8, we get our answer, although with 3^7 * 3^8 ~ 14.3 million computations on the last step.
If we ended here, the runtime would be ~80.9676380157

HOWEVER, since we can take advantage of the fact that some patterns like (1,1,1), (2,2,2), and (3,3,3) have the same number of ways of showing up, meaning that in general, we can do about 1/6th of the work (1/3!), bringing the runtime to:
Time Taken: 13.6176569462

which is pretty close to a 6x speedup over the naive solution :). Not bad right?



"""
