import time
import string
START = time.time()

SIZE = 11


def train_swap(train,position):
	global SIZE
	if position < 0: #last case, permuted all trains.
		return [train]
	new_train = train[:position] + train[position:][::-1]
	if position == SIZE - 2:
		return train_swap(new_train,position-1)

	new_train_list = []
	for i in xrange(position+1,SIZE-1):
		next_train = new_train[:i] + new_train[i:][::-1]
		new_train_list += train_swap(next_train,position-1)	
	return new_train_list

def main():
	train = range(1,SIZE-1) + [SIZE,SIZE-1]
	permutations = train_swap(train,SIZE-3)
	return permutations

answer = sorted(main())
solution = answer[2010]
print string.join([chr(i+64) for i in solution],'')


print "Time taken:", time.time() - START

"""
~/Desktop/python_projects/proj_euler $python prob336.py 
CAGBIHEFJDK
Time taken: 1.55418992043


Congratulations, the answer you gave to problem 336 is correct.

You are the 757th person to have solved this problem.

Return to Problems page.
"""
