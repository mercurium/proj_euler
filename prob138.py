import time
START = time.time()

x = [4]
y = [1]

for i in xrange(11):
    x.append(x[-1]*4+y[-1])
    y.append(x[-2])

print x
print y

sumz = sum([a**2 for a in x[:12]]) +  sum([b**2 for b in y[:12]])

print sumz
print "Time Taken:", time.time() - START

"""
LOL okay. So the problem gave us the two smallest cases, aka (16,17) and (272,273). Noticing that 272 = 17*16... and 273 = 17**2 -2**2, i was like huh...

Using the m, n construction, we get the values (4,1) and (17,4). Looking one further, we get (72,17). This leads me to the conclusion that the next value we want to find is located at:

(4x+y,x), given that (x,y) is the previous answer. This assumption seems to follow, and gives me the right answer, 

1118049290473932
Time Taken: 0.0254650115967
"""
