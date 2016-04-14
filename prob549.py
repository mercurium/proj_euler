import time, math
START = time.time()
SIZE  = 10**6

def pfactorGen(size): #for each number n, return some factor of it.
  stuff = [0,1,2] + [1,2] *(size/2-1)
  for i in xrange(3,size,2):
    if stuff[i] == 1:
      for j in xrange(i**2,size,i*2):
        stuff[j] = i
      stuff[i] = i
  return stuff

factor_list = pfactorGen(SIZE+1)
print "factors generated!"

def factor(num):
  factors = []
  while (factor_list[num] != num):
    factors.append(factor_list[num])
    num /= factor_list[num]
  if num != 1:
    factors.append(num)
  return factors

def powerGainedFromFactorial(num, power):
  return sum([power / num**x \
      for x in xrange(0, int(math.log(power, num) +1))])

cache = {}
def getSmallestNumReq(num, val):
  if val <= num:
    return val * num
  if (num,val) in cache:
    return cache[(num,val)]
  estimate = val * (num - 1) / num
  while powerGainedFromFactorial(num,estimate) < val:
    estimate += 1
  cache[(num,val)] = estimate * num
  return estimate * num


def getSmallestNumWithFactors(factors):
  factorMap = {}
  for factor in factors:
    if factor not in factorMap:
      factorMap[factor] = 1
    else:
      factorMap[factor] += 1
  return max([getSmallestNumReq(x, factorMap[x]) for x in factorMap.keys()])

def main():
  sumVal = 0
  for i in xrange(2,SIZE+1):
    factors    = factor(i)
    costOfNum  = getSmallestNumWithFactors(factors)
    sumVal    += costOfNum

  print sumVal
  print "Time Taken:", time.time() - START
  print len(cache)

main()

'''
  Congratulations, the answer you gave to problem 549 is correct.

  You are the 104th person to have solved this problem.


10^5:
  793183093
  Time Taken: 0.461635112762
10^6:
  64938007616
  Time Taken: 4.52511096001
10^8:
  476001479068717
  Time Taken: 476.378027916
  Time Taken: 364.408684015 (added in caching of expensive computations)


'''
