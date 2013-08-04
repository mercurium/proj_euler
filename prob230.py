import time
start = time.time()

def req(A,B,fib_lst, index,pos, item_index):
	if pos == 0: #if we recursed down to the 0th item, it's in the A item.
		return str(A)[item_index-1]
	if pos == 1: #if we recursed down to the 1st item, it's in B.
		return str(B)[item_index-1]

	if index < fib_lst[pos-2]: #if it's in the first half of the number...
		return req(A,B,fib_lst, index, pos -2, item_index)
	return req(A,B,fib_lst, index - fib_lst[pos-2], pos -1, item_index) #or else it's in the second half.

def executor(lim, A,B):
	dig = len(str(A))
	fib_lst = [1,1,2]
	while fib_lst[-1] * dig < lim:
		fib_lst.append(fib_lst[-1] + fib_lst[-2])
	return req(A,B,fib_lst, lim/dig, len(fib_lst) -1, lim%dig)

def main(lim):
	A = 1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679
	B = 8214808651328230664709384460955058223172535940812848111745028410270193852110555964462294895493038196
	return executor(lim,A,B)

def test(lim):
	A = 1415926535
	B = 8979323846 
	return executor(lim,A,B)


ans = ""
for i in xrange(18):
	ans =  main( (127 + 19*i) * 7**i) + ans
print ans
print "Time Taken:", time.time() - start
"""
Congratulations, the answer you gave to problem 230 is correct.

You are the 1714th person to have solved this problem.

16:59 ~/Desktop/python_projects/proj_euler $ python prob230.py 
850481152593119296
Time Taken: 0.000350952148438

"""
