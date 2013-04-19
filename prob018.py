testTriangle = [[0,3,0], [0, 7, 4, 0], [0, 2, 4, 6, 0], [0, 8, 5, 9, 3, 0]]

# r = row, c = column (list[r][c])
def maxGettingTo(lst, r, c):
  if r == 0: 
    return lst[0][1]
  return lst[r][c] + max(maxGettingTo(lst, r-1, c), maxGettingTo(lst, r-1, c-1))


print 'hi i work'
print maxGettingTo(testTriangle, 3, 0)
print maxGettingTo(testTriangle, 3, 1)
print maxGettingTo(testTriangle, 3, 2)
print maxGettingTo(testTriangle, 3, 3)
r = len(testTriangle) - 1

for c in range(0, len(testTriangle[r]) -2):
  print r
  print c
  print 'hi i dont work'
  print maxGettingTo(testTriangle, 3, 0)
  print maxGettingTo(testTriangle, r, c)

print max






