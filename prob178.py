#Okay, so the way this problem can be solved is by realizing that if you want to have 0-9, you either need 0123456789 or 9876543210 in there. Then once you have that, you can either insert more in the middle of the steps or add to the ends.

import time
import copy
start = time.time()
#right answer = 126461847755

lst = [0,0] + [1]*9 + [0] #0 to 9
lst_2 = [0,0]+[1]*8+[0,0] #0-8
lst_4 = [0,0]+[1]*9 + [0]
lst_3 = [0]*2+[1]*8+[0]*2 #1-8


#print lst
big_sum = 0
for i in range(0,40):
  temp = [0]*12
  temp2 = [0]*12
  temp3 = [0]*12
  temp4 = [0]*12
  sum = 0
  sum2 = 0
  sum3 = 0
  sum4 = 0
  for j in range(1,len(lst)-1):
    if j != len(lst)-2:
      temp2[j] = lst_2[j-1]+lst_2[j+1]
    if j != len(lst)-2 and j!= 1:
      temp3[j] = lst_3[j-1]+lst_3[j+1]
    if j!=1:
      temp4[j] = lst_4[j-1]+lst_4[j+1]
    temp[j] = lst[j-1] +lst[j+1]
    sum += temp[j]
    sum2 += temp2[j]
    sum3 += temp3[j]
    sum4 += temp4[j]
  lst = temp[:]
  lst_2 = temp2[:]
  lst_3 = temp3[:]
  lst_4 = temp4[:]
  if i+2 <= 40:
    big_sum += sum-sum2+sum3-sum4
  print sum-sum2+sum3-sum4, i+2
print big_sum

print "Time Taken: " + str(time.time()-start)
