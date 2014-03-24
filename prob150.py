import time
START = time.time()
ROWS = 1000
SIZE = 500500
t = 0
k = [0] * (SIZE)
for i in xrange(len(k)):
	t = (615949 * t + 797807) % (2**20)
	k[i] = t-2**19

rows =[]

for i in xrange(1,1001):
	rows.append(k[ i*(i-1)/2: i*(i+1)/2])

row_sums = []
for row in rows:
	sumz = [0]
	for i in range(0,len(row)):
		sumz.append(sumz[-1] + row[i])
	row_sums.append(sumz)

def row_sum(row, start, end):
	return row_sums[row][end] - row_sums[row][start]

min_sumz = 0
for start_row in xrange(0, ROWS):
	break
	for start_index in xrange(0,start_row+1):
		sumz = rows[start_row][start_index]
		for h in xrange(1,1000-start_row):
			sumz += row_sum(start_row+h, start_index, start_index+h+1)
			if sumz < min_sumz:
				min_sumz = sumz
				print min_sumz
	print start_row, min_sumz
	
print min_sumz
print "Time Taken:", time.time() - START

"""
-271248680
Time Taken: 87.0703659058

Congratulations, the answer you gave to problem 150 is correct.

You are the 1986th person to have solved the problem.

A subtriangle of this problem consists of two values, the start point and the height. We can split up the start point to be the row that it's in and the place in the row that it's at. Then, we can run the sum function over all sets of triangles. Each subtriangle can be computed in O(1) time by first figuring out the sum of the rows at each point and having sum(end) - sum(start) for each row. Then, we just increment the height of the triangle at each start point until we get the desired result.


"""
