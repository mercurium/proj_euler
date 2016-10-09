import time, string
START = time.time()
from itertools import combinations

def test(setz):
    SET_SIZE = len(setz)
    temp_set = set()
    for i in xrange(1,SET_SIZE):
        for j in combinations(range(SET_SIZE),i):
            k = sum( setz[l] for l in j)
            if k in temp_set:
                return False
    return True

def bb_search(solution):
    if len(solution) == 7 and test(solution) == True:  #case where we've found a good solution.
        return solution
    if not test(solution):  #The current set doesn't work... =/
        return -1
    new_sol   = solution[:]
    lim       = solution[0] + solution[1]
    lim_start = solution[-1] + 1
    new_sol.append(lim_start)
    ans       = bb_search(new_sol)
    while ans == -1 and new_sol[-1] < lim:
        new_sol[-1] +=1
        ans = bb_search(new_sol)
    return ans


for i in xrange(20,30):
    for j in xrange(i+1,40):
        print i,j
        ans = bb_search([i,j])
        if ans != -1:
            print ans, sum(ans)
            break
    if ans != -1:
        break

ans = [str(i) for i in ans]
ans = string.join(ans,'')
print ans

print "Time Taken:", time.time() - START

"""
=.=;;

Turns out by applying that "rule" that was mentioned, you can get the optimal set for this problem... so I didn't even need to write this code. wtf euler...

[20, 31, 38, 39, 40, 42, 45] 255
20313839404245
Time Taken: 1.34041786194
"""


