temp_lst = [0]*10**6
prime_set = set([])
for i in range(2,len(temp_lst)):
  if temp_lst[i] == 0:
    prime_set.add(i)
    for j in range(2*i,len(temp_lst),i):
      temp_lst[j] +=1
