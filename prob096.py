import string
import time
import random
start = time.time()


def branch_and_bound(pos, solution, edge_dict, order):

    largest_seen = max(solution)
    if largest_seen  <= 9 and min(solution) >= 0:  #the done case =P
        return solution 
    if largest_seen > 9:  #if we got bigger than we wanted...
        return -1

    for i in order:
        if solution[i] == -1:
            set_check = set([solution[c] for c in edge_dict[i]])
            if -1 in set_check: 
                set_check.remove(-1)
            if len(set_check) == 8:
                not_seen = list(set(range(1,10)).difference(set_check))[0]
                solution[i] = not_seen
            elif len(set_check) == 9:
                return -1

    next_val = order[pos]
    while solution[next_val] != -1 and pos >= 0 and pos < len(order)-1:
        pos +=1
        next_val = order[pos]

    order = order[pos:]
    pos = 0 

    temp_set = set([ solution[c] for c in edge_dict[next_val]])
    
    for color in xrange(1,10):
        if color not in temp_set:
            new_sol = solution[:]
            new_sol[next_val] = color
            ans = branch_and_bound(pos,new_sol,edge_dict,order[1:])
            if ans != -1:
                return ans
    return -1   #none of the colors above work for it...


data_file = open("sudoku.txt",'r')
data = data_file.read()

data = string.split(data.strip(),'\n')
grids = []

for grid in range(50):
    grids.append(data[10*grid+1:10*grid+10])


edge_dict = dict()
for i in range(81):
    edge_dict[i] = set()
    row, col = i/9, i % 9
    grid_sq_row, grid_sq_col = row/3, col/3
    for j in range(9):
        edge_dict[i].add(col + j * 9)
        edge_dict[i].add(j + row*9)

    for a in range(3):
        for b in range(3):
            edge_dict[i].add( grid_sq_row *27 + grid_sq_col * 3 + a*9 + b)
    edge_dict[i].remove(i)


skipped_grids = []
#50 test cases, 10 lines ea...
sumz = 0
skip_count = 0
for num_grid in range(50):
    grid = grids[num_grid]
    nodes = []
    for row in grid:
        for node in row:
            nodes.append(int(node))
            if nodes[-1] == 0: nodes[-1] = -1

    solution = branch_and_bound(0, nodes, edge_dict, range(81))
    print num_grid, time.time() - start

    sumz += solution[0] * 100 + solution[1]*10+solution[2]
    iterations = 0

print sumz
print "Time Taken: ", time.time() -start


"""

Time Taken:  0.457056045532

Congratulations, the answer you gave to problem 96 is correct.

You are the 7889th person to have solved this problem.

You have earned 1 new award:

Centurion: Solve one hundred consecutive problems

For this problem, I used my graph coloring algorithm from the discrete optimization class

"""
