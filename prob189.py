#NOTE TODO need to solve it

import time
START = time.time()
from itertools import product

valCount = {('1',):1, ('2',):1, ('3',):1}
for row in range(2,9):
    rowOverall = 0
    for combo in product('123', repeat=row):
        if row == 8:
            if '1' not in combo or ('3' in combo and '2' not in combo):
                continue
            if '2' in combo and '3' in combo:
                if not(combo.index('1') < combo.index('2') < combo.index('3')):
                    continue
            elif '2' in combo:
                if combo.index('1') > combo.index('2'):
                    continue

        valCount[combo] = 0
        for oldCombo in product('123', repeat=row-1):
            currentCount = valCount[oldCombo] 
            for spot in range(len(combo)-1):
                currentCount *= (3 - len(set([oldCombo[spot], combo[spot], combo[spot+1]])))
            valCount[combo] += currentCount


        if row != 8: 
            rowOverall += valCount[combo]
        else:
            if len(set(combo)) == 1:
                rowOverall += valCount[combo] * 3
            else:
                rowOverall += valCount[combo] * 6
    print row, rowOverall
    

print "Time Taken:", time.time() - START

"""

Congratulations, the answer you gave to problem 189 is correct.

You are the 1146th person to have solved this problem.

10834893628237824
Time Taken: 80.9676380157 
Time Taken: 19.9419779778 once I accounted for symmetry
H = x:
1: 3
2: 24
3: 528

"""
