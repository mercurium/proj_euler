import string
import copy
import time

start = time.time()

def compute(items,num_left): #items is given in a dictionary.
  def remove_extra(items, val, row, col):
    for i in range(9): #removing those in the row
      if i!= col and val in items[(i,col)]:
        items[(i,col)].remove(val)
    for j in range(9):
      if j!= row and val in items[(row,j)]:
        items[(row,j)].remove(val)
    
    return items
  
  checked = [[0]*9 for x in range(9)]
  for row in range(9):
    for col in range(9):
      if type(items[(row,col)] == int and checked[i][j] == 0:
        items = remove_extra(items,items[(row,col)],row,col)
        checked[row][col] = 1

  return 0



data_file = open("sudoku.txt",'r')
data = data_file.read()

data = string.split(data.strip(),'\n')



#50 test cases, 10 lines ea...
sumz = 0
for i in range(0,1):
  items = dict()
  count = 81
  for j in range(9):
    for k in range(9):
      val = int(data[10*i+j+1][k])
      if val != 0:
        items[(j,k)] = set([val])
        count -=1
      else:
        items[(j,k)] = set([1,2,3,4,5,6,7,8,9])
  sumz += compute(items, count)

print sumz
print "Time Taken: ", time.time() -start
