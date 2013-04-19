from math import factorial as fa
th = [4,3,3,2,2,2,2,1,1,1,1,1,0,0,0,0,0]
tw = [0,1,0,3,2,1,0,4,3,2,1,0,6,5,4,3,2]
on = [0,1,3,0,2,4,6,1,3,5,7,9,0,2,4,6,8]

print len(th)
sumz = 0
for i in range(0,len(th)):
  a = 10-on[i]-tw[i]-th[i] #numbers untouched by removal
  b =(6**a) *(2**on[i]) #bottom of 18!/(3!^a*2^ones[i])
  c= fa(th[i]) * fa(tw[i]) *fa(on[i]) #part for 10C(a,b,c)
  d = fa(10)/(c* fa(a)) # 10C(a,b,c)
  e = (fa(18)*d)/b
  print a,b,c,d, e
  sumz += e

#this part is to account for no leading zeroes
print sumz *9 /10

#137225088000
#wrong answers:
#20748433305600000
#227372725275696000

#right answer:
#227485267000992000

#note: took me a while to get this one since i thought there were 16 partitions of 12 instead of 17 (with each number <= 3 and no more than 10 numbers)


#OH! Okay, I got it. The way I did this was by listing out all possible combinations of 3a+2b+c = 12...


