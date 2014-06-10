import time,string
from itertools import permutations
START = time.time()

iterations = 0
maxSeen = 0
for perm in permutations('1234567890'):
    for cut1 in range(1,3):
        num1 = int(string.join(perm[:cut1],''))
        for cut2 in range(cut1+1, len(perm)-1):
            iterations +=1
            num2 = int(string.join(perm[cut1:cut2],''))
            num3 = int(string.join(perm[cut2:],''))
            prod1 = num1 * num2
            prod2 = num1 * num3

            if set([int(x) for x in (str(prod1) + str(prod2))]) == set(range(0,10)) and len(str(prod1) + str(prod2)) == 10:
                concatProd = int(str(prod1) + str(prod2))
                if concatProd > maxSeen:
                    maxSeen = concatProd
                    print concatProd, num1, num2, num3, prod1, prod2
    if iterations % 2**14 == 0:
        print iterations

print "Time Taken:", time.time() - START

"""
Okay, I'm going to have to admit, I used a pretty bad solution for this problem. First, I iterated over all possible orderings of 0 to 9, and then over all possible splittings of that permutation into three numbers. After that, I just waited until a nice looking answer popped out, and voila, I plugged it in and it was right... :D;;


Congratulations, the answer you gave to problem 170 is correct.

You are the 1102nd person to have solved this problem.

Answer: 9857164023
27 x 36508 = 985716
27 x 149 = 4023

"""
