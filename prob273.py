import time
start = time.time()


numbers = {5:(1,2),13:(2,3),17:(1,4),29:(2,5),37:(1,6),41:(4,5),53:(2,7),61:(5,6),73:(3,8),89:(5,8),97:(4,9),101:(1,10),109:(3,10),113:(7,8),137:(4,11),149:(7,10)}




print "Time Taken:", time.time()-start


"""


(a^2+b^2)(c^2+d^2) = (ac-bd)^2+(ad+bc)^2
                   = (ac+bd)^2+(ad-bc)^2
(from http://en.wikipedia.org/wiki/Brahmagupta%E2%80%93Fibonacci_identity )

5 13 17 29 37 41 53 61 73 89 97 101 109 113 137 149
are the numbers of the form 4k+1 < 150

5 1 2
13 2 3
17 1 4
29 2 5
37 1 6
41 4 5
53 2 7
61 5 6
73 3 8
89 5 8
97 4 9
101 1 10
109 3 10
113 7 8
137 4 11
149 7 10
"""
