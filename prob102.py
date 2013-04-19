import string
import time
start = time.time()

true, false = True, False
temp = open('triangles.txt', 'r')
lst = string.split(temp.read(),'\n')[:-1]

for i in range(0, len(lst)):
  lst[i] = string.split(lst[i],',')

for i in range(0, len(lst)):
  for j in range(0, len(lst[i])):
    lst[i][j] = int(lst[i][j])

def slope_origin(x,y):
  return y * 1.0/x

def slope_ab(pt1,pt2, pt3):
  a, b = (pt2[0]-pt1[0]), (pt3[0]-pt1[0])
  if a == 0 and b==0: return 0,0
  if a == 0: return 0, (pt3[1]-pt1[1])*1.0/(pt3[0]-pt1[0])
  if b ==0: return (pt2[1]-pt1[1])*1.0/(pt2[0]-pt1[0]) , 0
  return (pt2[1]-pt1[1])*1.0/(pt2[0]-pt1[0]) , (pt3[1]-pt1[1])*1.0/(pt3[0]-pt1[0])

def lowest_pt(lst):
  if lst[0] < lst[2] and lst[0] < lst[4]:
    return (lst[0],lst[1]), (lst[2],lst[3]), (lst[4],lst[5])
  if lst[2] < lst[4] and lst[2] < lst[0]:
    return (lst[2],lst[3]), (lst[0],lst[1]), (lst[4],lst[5])
  return (lst[4],lst[5]), (lst[2],lst[3]), (lst[0],lst[1])

def ord_check(lst):
  if lst[0] > 0 and lst[2] > 0 and lst[4] > 0: return False
  if lst[0] < 0 and lst[2] < 0 and lst[4] < 0: return False
  if lst[1] > 0 and lst[3] > 0 and lst[5] > 0: return False
  if lst[1] < 0 and lst[3] < 0 and lst[5] < 0: return False
  return True


def slope_in(lst):
  minz, pt1, pt2 = lowest_pt(lst)
  slope_or = slope_origin(minz[0],minz[1])
  s1, s2 = slope_ab(minz, pt1, pt2)
  
  if ord_check(lst) and ((s1 < slope_or and s2 > slope_or) or (s1 > slope_or and s2 < slope_or) ):
    return true
  return false

sumz = 0
for i in range(0,len(lst)):
  if slope_in(lst[i]):
    sumz += 1
print sumz
print "Time Taken: " + str(time.time()-start)
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
