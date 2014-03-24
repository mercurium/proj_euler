import time
START = time.time()

SIZE = 10**5
sumz = 0
for i in xrange(2,SIZE):
    for j in xrange(1,i):
        a = j*j
        b,c = i*i%j, (i*i)/j
        if a == b*c:
            print j,b,c,i,i**2, j*1.0/i
            sumz += i**2

print "Time Taken:", time.time() - START

"""
2 1 4 3 9 0.666666666667
72 36 144 102 10404 0.705882352941
75 25 225 130 16900 0.576923076923
92 8 1058 312 97344 0.294871794872
360 81 1600 759 576081 0.474308300395
1472 512 4232 2496 6230016 0.589743589744
2420 1936 3025 2706 7322436 0.894308943089
2450 1225 4900 3465 12006225 0.707070707071
5760 5184 6400 6072 36869184 0.948616600791
5292 3969 7056 6111 37344321 0.865979381443
7452 5832 9522 8424 70963776 0.884615384615
4392 432 44652 14004 196112016 0.313624678663
6534 1089 39204 16005 256160025 0.40824742268
30870 21609 44100 36897 1361388609 0.836653386454
25872 12544 53361 37156 1380568336 0.696307460437



"""
