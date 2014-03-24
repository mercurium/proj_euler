import time
START = time.time()


start_position = 0
total_sum = 200

coins = [200,100,50,20,10,5,2,1]

def recurse(val, coin):
	if coin == 8 or val < 0: #We went over our boundaries... =/
		return 0
	if coin == 7: #Only one choice at this point
		return 1
	# Either add a new coin of the current type or move on.
	return recurse(val, coin+1) + recurse(val - coins[coin],coin)

print recurse(total_sum,start_position)

print "Time Taken:", time.time() - START
