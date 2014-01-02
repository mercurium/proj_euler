import time
START = time.time() 

SIZE = 50
LAYERS = 100
val_dict = dict()

for i in xrange(1,SIZE):
	for j in xrange(i,SIZE):
		for k in xrange(j,SIZE):
			for layer in range(LAYERS):
				val = 2 * (i*j+j*k+k*i) + layer * (4*(i+j+k-1)) + 4*layer**2
				if val in val_dict:
					val_dict[val] +=1
				else:
					val_dict[val] = 1

maxz = 0
for i in val_dict:
	if val_dict[i] > maxz:
		print i, val_dict[i]
		maxz = val_dict[i]
print "Time Taken:", time.time() - START

"""
formula for this is:
2(ab+bc+ca) + n(4(a+b+c-1)) + 4n^2

Math for this formula worked out below:

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
