import time
START = time.time()
from itertools import permutations


operations = {0:"concat",1:"add",2:"subtract",3:"multiply",4:"divide"}
answers = set()
def do_operation(n,lst):
    if len(lst) == 0:
        if n 
        answers.add(n)
        return
    lst = lst[:]
    nextVal = lst.pop()
    do_operation(n+nextVal,lst)
    do_operation(n-nextVal,lst)
    do_operation(n*nextVal,lst)
    do_operation(n/nextVal,lst)
    do_operation(int(str(n)+str(nextVal)),lst)


for perm in permutations([1,2]):
    perm = list(perm)
    n =  perm.pop()
    do_operation(n,perm)

print answers

print "Time Taken:", time.time() - START
