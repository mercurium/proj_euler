import time
start = time.time()

b_count = 40
w_count = 60

values = {}
#init at 60,40,0,1
def counter(b_left,w_left,b_num,w_num):
  if (b_left,w_left,b_num,w_num) in values:
    return values[(b_left,w_left,b_num,w_num)]
  
    
  if b_num == b_left and w_num == w_left:
    values[(b_left,w_left,b_num,w_num)] = 1
    return 1
  
  #only increment black when white overflows, like incrementing digits
  if w_num > w_left:
    return counter(b_left,w_left,b_num+1,0)
  
  if b_num > b_left:
    return 0
    
  #either subtrack it from the running sum
  use_item = counter(b_left-b_num,w_left-w_num,b_num,w_num)
  #or increment white
  inc_w = counter(b_left,w_left,b_num,w_num+1)
  
  #return their sum
  values[(b_left,w_left,b_num,w_num)] = use_item+ inc_w
  return use_item+ inc_w


for b_leftz in range(0,b_count+1):
  for w_leftz in range(0,w_count+1): 
    for b_numz in range(b_count,-1,-1):
      for w_numz in range(w_count,0,-1):
        counter(b_leftz,w_leftz,b_numz,w_numz)

print values[(b_count,w_count,0,1)]
print "Time Taken:", time.time() - start

"""
Congratulations, the answer you gave to problem 181 is correct.
You are the 932nd person to have solved this problem.

~/Desktop/python_projects/proj_euler $python prob181.py
83735848679360680
Time Taken: 6.81846213341


YESSSS!!!

Anyways, the main idea behind this is: just like with partitions, we want to either break off a number 'n' or we don't want to, in which case we increment the counter for it, so we can either add 'n+1' or increment again. etc.

That's the idea for the partitions of one item. Now for a partition of 2 dimensions, we need some way of deciding if a partition is "greater" than another. I did this by saying 'a' > 'b' if a[#black] > b[#black] or a[#black] == b[#black] and a[#white] > b[#white].

Thus, we add the smallest possible partitions to the group first and then we work our way up.

Also, a mistake I made earlier is incrementing either white or black at each step. I should only increment black if white is over the limit.
"""
