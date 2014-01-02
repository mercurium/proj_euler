import time
START = time.time() 

SIZE = 10000
LAYERS = 100
val_dict = dict()

for i in xrange(1,SIZE):
	for j in xrange(1,i+1):
		if (i+1)*(j+1) + 1 > 25000: break

		for k in xrange(1,j+1):
			a,b = 2*(i*j+j*k+k*i), 4*(i+j+k-1)
			if a > 25000: break

			for layer in range(LAYERS):
				val = a + layer * b + 4*layer**2
				if val > 25000: break

				if val in val_dict:
					val_dict[val] +=1
				else:
					val_dict[val] = 1
	print i


for key in sorted(val_dict.keys()):
	if val_dict[key] == 1000:
		print key
		break
print "Time Taken:", time.time() - START













"""
 Congratulations, the answer you gave to problem 126 is correct.

You are the 2215th person to have solved this problem.

Answer: 18522
Time Taken: 4.04020619392

Okay, so the logic for this problem was as such. I first figured out that the nth layer had 2(ab+bc+ca) + 4n(a+b+c-1) +4n^2 blocks.
Then I iterated over this list, and whenever i got to numbers that seemed to be too big to be the right answer (since some numbers <20000 were already having results of 1000+, it couldn't be too big), so I capped it at 25000. Then, after the iteration, I got the answer.... :D;;;...

I just kept it going till it exhausted all possible results for plugging in to that field.

Normally I would clean up my code below, but I like having my scratch notes below... :x


formula for this is:
2(ab+bc+ca) + 4n(a+b+c-1) + 4n^2

Math for this formula worked out below (scratch work):

First layer = 2(ab+bc+ac)
second layer = 2(ab+bc+ac) + 4(a+b+c)

1x1x1:
f   1, 7, 25, 63, 129, 231
f'     6, 18, 38,  66, 102
f''       12, 20,  28,  36
f'''           8,   8,   8


(1+0) + (4+1) + (1+0) = 7
(1+0) + (4+1) + (9+4) + (4+1) + (1+0) = 25
(1+0) + (4+1) + (9+4) + (16+9) + (9+4) + (4+1) + (1+0) = 63


1x2x3
0, 6, 28, 74, 152, 270, 436
   6, 22, 46, 78,  118, 166,
      16, 24, 32,   40,  48
           8,  8,    8
			   0,    0


2x2x2
0, 8, 32, 80, 160, 280
   8, 24, 48,  80, 120
      16, 24,  32,  40
           8,   8,   8

k, k, k, ?
   k, k, ?
      k, 
         k

a, b, c, x, y, ...
   d, e, w,w0,w1   <--- We want this row.
      f, z,z0,z1,...
         8, 8, 8, ...

f+8 = z
z+8= z0
z0+8=z1
e+z = w
w+z0=w0 = w+z+8 = f+w+16
w0+z1=w1 = w0+z0+8 = w0+z+16 = w+2z+24 = w+2f+40
c+w = x


abc, abc+2(ab+bc+ac), abc+4(ab+bc+ac) + 4(a+b+c)

2(ab+bc+ac) + (n-1)(4(a+b+c)) + 8t


"""
