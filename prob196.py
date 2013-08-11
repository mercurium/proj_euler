import time
START = time.time()
from primes import m_r

pos = [5678027, 7208785]

def neighbors(n,row):
	row_start = row*(row-1)/2 + 1
	pos = n - row_start
	if pos != 0:
		if row % 2 == 0:
			neighbors = [ n-row+2,n-row,n+row]
		else:
			neighbors = [n-row+1,n+row-1,n+row+1]
	else:
		neighbors = [n+row,n+row+1,n-row+1,n-row+2]
	return neighbors	

sumz = 0
for p in pos:
	i = p*(p-1)/2+1
	while i < p*(p+1)/2 - 1:
		if m_r(i):
			neigh = neighbors(i,p)
			neigh_sum = sum([m_r(x) for x in neigh])
			if neigh_sum >= 2:
				sumz += i
			else:
				for num in neigh:
					row = p-1 if num < i else p+1
					if m_r(num):
						neigh_sum = sum([m_r(x) for x in neighbors(num,row)]) 
						if neigh_sum >= 2:
							sumz +=i
							break
		i+=1
	print sumz
print sumz
print "Time Taken:", time.time() - START

"""
Congratulations, the answer you gave to problem 196 is correct.

You are the 1225th person to have solved this problem.


322303240771079935
Time Taken: 284.793769121

01:31 ~/Desktop/python_projects/proj_euler $ python prob196.py 
79697256800321526
322303240771079935
Time Taken: 100.014121056 (on my desktop)


was the answer on my laptop, I imagine it would be much faster on my desktop
"""
