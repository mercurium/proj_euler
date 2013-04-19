import math

twos = [2**x for x in xrange(1,100)]

fracs = [(17,91),(78,85),(19,51),(23,38),(29,33),(77,29),(95,23),(77,19),(1,17),(11,13),(13,11),(15,2),(1,7),(55,1)]

val = 2
count = 0
values = []

while val < 2**100:
  for i in fracs:
    if val%i[1] == 0:
      count+=1
      val = val *i[0] /i[1]
      break
  if val in twos:
    print int(math.log(val,2)), count
    values.append(count)

print values
