import time, math
from math import factorial as fa
START = time.time()
SIZE = 10**9
MOD = 1234567891

def perm(n,r):
    prod = 1
    for i in xrange(0,r):
        prod = (prod * (n-i))
    return prod

def recurse_count(depth, min_num, size, DEPTH, num_count, prod ): #min num has to be at least 2.
    if size < min_num**depth:
        return 0
    if depth == 1:
        p = perm(SIZE,DEPTH)
        n = ((size-min_num)*p)/ (prod * fa(num_count))
        n += p/(prod * fa(num_count+1))
        return n

    sumz = 0
    sumz += recurse_count(depth-1, min_num, size/min_num, DEPTH, num_count+1, prod)
    for i in xrange(min_num+1, size/min_num+1):
        if i > size/i:
            break
        sumz += recurse_count(depth-1,i, size/i, DEPTH, 1, prod * fa(num_count))

    return sumz

count = 1
for depth in xrange(1,int(math.log(SIZE,2)+1)):
    num = recurse_count(depth,2,SIZE, depth, 0, 1)
    count += num
    count %= MOD
    print depth, count, num % MOD, time.time() - START


print count

print "Time Taken:", time.time() - START

"""
Congratulations, the answer you gave to problem 452 is correct.

You are the 35th person to have solved this problem.

Return to Problems page.


So the algorithm I used for this problem was, for each int s < log(SIZE,2), figure out the number of products a*b*...*n_s <= SIZE, where a,b,...n_s > 1. This can be done by using ugly recursive for loops, but in reality, it's not that bad since the larger loops have few choices for a,b,..etc.

Answer: 345558983
Time Taken: 475.002918005
Time Taken: 403.300715208 (on desktop)


~/proj_euler $python prob452.py 
1 1117160546 1117160545 4.48226928711e-05
2 503214651 620621996 0.0541160106659
3 913447321 410232670 2.76046681404
4 383865615 704986185 24.1977050304
5 343791104 1194493380 89.4937529564
6 571529580 227738476 185.22782588
^L7 1069505724 497976144 286.599858999
8 1080301195 10795471 360.027160883
9 1041098959 1195365655 407.326979876
10 554213014 747681946 436.316274881
11 1061814824 507601810 451.971356869
12 567585873 740338940 460.874964952
13 395943368 1062925386 465.592012882
14 1124689687 728746319 468.320518017
15 968590878 1078469082 469.906841993
16 27872295 293849308 470.944206953
17 202435645 174563350 471.639184952
18 232713525 30277880 472.269335032
19 674446948 441733423 472.698899031
20 677703160 3256212 472.979082823
21 1150958453 473255293 473.220373869
22 726840514 810449952 473.441326857
23 996860852 270020338 473.653156042
24 127891733 365598772 473.867295027
25 1105827789 977936056 474.08552599
26 56646887 185386989 474.311257839
27 165330935 108684048 474.537729979
28 404690556 239359621 474.76440382
29 345558983 1175436318 475.002889872
345558983
Time Taken: 475.002918005

"""
