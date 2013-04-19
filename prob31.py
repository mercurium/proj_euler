import time
start = time.time()



valz = 200

coins = [200,100,50,20,10,5,2,1]

def recurse(val, coin):
  if coin == 8 or val < 0:
    return 0
  if coin == 7:
    return 1
  return recurse(val, coin+1) + recurse(val - coins[coin],coin)

print recurse(valz,0)

print "Time Taken: " + str(time.time()-start)
