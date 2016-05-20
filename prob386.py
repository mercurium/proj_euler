import time
START = time.time()




print "Time taken:", time.time() - START


'''
Theory:
  If I take the ncr that has the largest number, then that constitutes the antichain

  111 -> 3 (2)
  211 -> 4 (2)
  221 -> 5 (2)
  222 -> 7 (3)

  311 ->

4 * 9 * 25 = 900

a^2 x b^2 x c (5)
  0 1 2 3 4 5
  1 3 5 5 3 1
  a^2, b^2, ab, ac, bc

a^3 x b x c (4)
  0 1 2 3 4 5
  1 3 4 4 3 1
  a^2, b^2, ab, ac, bc

a^2 x b x c (4)
  0 1 2 3 4
  1 3 4 3 1
  a^2, ab, ac, bc

a^2 x b^2 x c^2 = 27 elements (7)
  a^2b, a^2c, b^2a, b^2c, c^2a, c^2b, abc (7)
  1, a,b,c, a^2b^2c, ab^2c^2, a^2bc^2, a^2b^2c^2
  0,1,2,3,4,5,6
  1,3,6,7,6,3,1

a^4b^2 (3)
  0,1,2,3,4,5,6
  1,2,3,3,3,2,1

a x b x c x d
  0 1 2 3 4
  1 4 6 4 1

a^2 x b x c x d (7)
  0 1 2 3 4 5
  1 4 7 7 4 1

a^4 x b^4 x c^4 (19)
  0  1  2  3  4  5  6
  1  3  6 10 15 18 19

72 = 2^3 x 3^2
  8, 12, 18

a^k x b^j = min(k,j) + 1
'''
